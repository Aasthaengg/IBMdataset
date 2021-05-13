import collections
n,k=map(int,input().split())
a=list(map(int,input().split()))
a=collections.Counter(a)
values,counts=zip(*a.most_common())
l=len(values)
ans=0
i=0
while l>k:
  ans=ans+counts[len(values)-i-1]
  i=i+1
  l=l-1

print(ans)