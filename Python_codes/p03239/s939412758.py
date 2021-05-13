n,t = map(int,input().split())
ans = -1
for i in range(n):
    c,ti = map(int,input().split())
    if ti<=t:
        if ans==-1:
            ans = c
        else:
            ans = min(ans,c)
if ans==-1:
    print("TLE")
else:
    print(ans)