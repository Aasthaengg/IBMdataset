K,A,B=map(int,input().split())

cnt=K-A+1
count=cnt//2
cnt=A-1
cnt+=count*2
balance=K-cnt
ans=0
ans+=A
ans+=(B-A)*count
ans+=balance
#print(ans)
ans=max(ans,K+1)
print(ans)