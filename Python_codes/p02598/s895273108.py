from math import ceil
n,k = map(int,input().split())
a = list(map(int,input().split()))

def cut(x):
  t = 0
  for i in a:
    if i <= x:
      continue
    t += ceil(i / x) - 1
  return t <= k

l,r=0,10**9
while l+1 < r:
  x = l + (r-l)//2
  if cut(x):
    r = x
  else:
    l = x
print(r)