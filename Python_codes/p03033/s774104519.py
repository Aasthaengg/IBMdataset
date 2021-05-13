from bisect import bisect_left as b;n,q=map(int,input().split());w=sorted([list(map(int,input().split()))[::-1]for _ in[0]*n]);p=[int(input())for _ in[0]*q];a=[-1]*q;o=[-1]*q
for x,t,s in w:
  l,r=b(p,s-x),b(p,t-x)
  while l<r:
    if o[l]+1:l=o[l]
    else:a[l],o[l]=x,r;l+=1
print(*a)