n=int(input())
a=[]
b=[]
for i in range(n):
  aa,bb=map(int,input().split())
  a.append(aa)
  b.append(bb)
m=0
for i in range(n-1,-1,-1):
  a[i]+=m
  if a[i]%b[i]:m+=b[i]-a[i]%b[i]
print(m)