n=int(input())
a=[0]+[int(input()) for _ in range(n)]
d=[False]*(n+1)
i=1
ans=0
while d[i]==False and i!=2:
    d[i] = True
    ans += 1
    i=a[i]
if d[i]:
    print(-1)
else:
    print(ans)