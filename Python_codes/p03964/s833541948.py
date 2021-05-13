n=int(input())
f=lambda:map(int,input().split())
a,b=f()
for _ in range(1,n):
  c,d=f()
  t=max(1,0--a//c,0--b//d)
  a,b=c*t,d*t
print(a+b)