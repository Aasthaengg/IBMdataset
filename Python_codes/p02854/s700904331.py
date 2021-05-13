n=int(input())
a=list(map(int,input().split()))
sm=sum(a)
x=[a[0]]
y=[sm-a[0]]
for i in range(1,n):
  x.append(x[i-1]+a[i])
  y.append(sm-x[i])
min=9999999999
for (p,q) in zip(x,y):
  sa=abs(p-q)
  if sa<min:
    min=sa

print(min)