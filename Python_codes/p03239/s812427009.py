N,T=map(int,input().split())
ans=1e9+7
for i in range(N):
    c,t=map(int,input().split())
    if t<=T and c<ans:
        ans=c
if ans==1e9+7:
    print("TLE")
else:
    print(ans)