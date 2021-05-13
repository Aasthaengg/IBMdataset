n,k=map(int,input().split())
a=list(map(int,input().split()))
ball=[0]*n
s=set()
for i in range(n):
    ball[a[i]-1]+=1
    s.add(a[i]-1)
kind=len(s)
ans=0
ball.sort()
for i in range(n):
    if ball[i]==0:
        continue
    if kind>k:
        kind-=1
        ans+=ball[i]
print(ans)