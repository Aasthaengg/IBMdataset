n,k=map(int,input().split())
s = list(input())
cnt=0
now=s[0]
for i in range(1,n):
    if now==s[i]:continue
    else:
        cnt+=1
        now=s[i]

ans=n-1-cnt
#syo=cnt//2
#print(ans)
print(min(n-1,ans+2*k))
