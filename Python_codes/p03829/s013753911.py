n,a,b=map(int,input().split())
x=list(map(int,input().split()))
ct=0
for i in range(n-1):
  d=x[i+1]-x[i]
  if d*a<b:ct+=d*a
  else:ct+=b
print(ct)