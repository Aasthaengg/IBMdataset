from bisect import bisect_left

n,q=map(int,input().split())
work=[list(map(int,input().split())) for _ in range(n)]
work=sorted(work,key=lambda x:x[2])
pos=[int(input()) for _ in range(q)]
ans=[-1]*q
checked=[-1]*q
for s,t,x in work:
  l=bisect_left(pos,s-x)
  r=bisect_left(pos,t-x)
  while l<r:
    if checked[l]==-1:
      checked[l]=r
      ans[l]=x
      l+=1
    else:
      l=checked[l]
for i in ans:
  print(i)