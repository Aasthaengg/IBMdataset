from math import sqrt
N,D=map(int,input().split())
ans = 0
for i in range(N):
    x,y=map(int,input().split())
    dist = sqrt(x*x + y*y)
    if (dist <= D ):
      ans+=1
print(ans)
