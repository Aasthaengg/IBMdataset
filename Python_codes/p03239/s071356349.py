N,T=map(int,input().split())
ans=[]
cnt=0
for i in range(N):
    c,t=map(int,input().split())
    if t<=T:
        ans.append(c)
        cnt=1
print('TLE' if cnt==0 else min(ans))