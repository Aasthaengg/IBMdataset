N,T=map(int,input().split())
ans=-1
for i in range(N):
    c,t=map(int,input().split())
    if t<=T:
        if ans==-1:
            ans=c
        else:
            if ans>c:
                ans=c
if ans==-1:
    print("TLE")
else:
    print(ans)