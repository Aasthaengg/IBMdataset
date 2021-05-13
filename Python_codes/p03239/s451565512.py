n,time=map(int,input().split())
c=[]
t=[]
for i in range(n):
    a,b=map(int,input().split())
    c.append(a)
    t.append(b)
ans=10**10
for i in range(n):
    if t[i]<=time:
        ans=min(ans,c[i])

print(ans if ans!=10**10 else "TLE")