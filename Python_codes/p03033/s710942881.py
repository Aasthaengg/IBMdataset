from bisect import bisect_left,bisect_right
n,q=map(int,input().split())
w=[list(map(int,input().split()))[::-1]for _ in range(n)]
p=[int(input())for _ in range(q)]
w.sort()
ans=[-1]*q
to=[-1]*q
for x,t,s in w:
  l,r=bisect_left(p,s-x),bisect_left(p,t-x)
  while l<r:
    if to[l]==-1:
      ans[l]=x
      to[l]=r
      l+=1
    else:
      l=to[l]
print(*ans)