n,m=[int(x) for x in input().split()]
ac=[0]*n
wa=[0]*n
a=0
b=0
for i in range(m):
  P,s=input().split()
  p=int(P)-1
  if s=="AC":
    if ac[p]==0:
      ac[p]=1
      a+=1
      b+=wa[p]
  else:
    if ac[p]==0:
      wa[p]+=1
print(a,b)