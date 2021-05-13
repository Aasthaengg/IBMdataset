from math import ceil
n,a,b=map(int,input().split())
h=[int(input()) for i in range(n)]
h.sort(reverse=True)
ok,ng=10**9,0
while ok-ng>1:
  mid=(ok+ng)//2
  damage=mid*b
  addition=mid
  flag=True
  for i in range(n):
    if h[i]<=damage:
      continue
    else:
      if addition>=ceil((h[i]-damage)/(a-b)):
        addition-=ceil((h[i]-damage)/(a-b))
      else:
        addition-=ceil((h[i]-damage)/(a-b))
        flag=False
        break
  if flag:
    ok=mid
  else:
    ng=mid
print(ok)