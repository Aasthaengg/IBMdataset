from collections import defaultdict
N=int(input())
alist=list(map(int,input().split()))

adic=defaultdict(int)
for a in alist:
  adic[a]+=1
alist2=list(adic.items())
alist2.sort(reverse=True)
#print(alist2)

x1,x2=0,0
for a2 in alist2:
  if a2[1]>=4:
    x1=max(x1,a2[0])
    x2=max(x2,a2[0])
  elif a2[1]>=2:
    if x1==0:
      x1=a2[0]
    else:
      x2=a2[0]

  if x1*x2>0:
    print(x1*x2)
    break
else:
  print(0)