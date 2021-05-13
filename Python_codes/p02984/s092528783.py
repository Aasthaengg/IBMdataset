n=int(input())
a=list(map(int,input().split()))
ev=[]
for i in range(n):
  if i%2==1:ev.append(a[i])
x=[0]*n
x[0]=sum(a)-2*sum(ev)
for i in range(1,n):
  x[i]=2*a[i-1]-x[i-1]
print(*x)

