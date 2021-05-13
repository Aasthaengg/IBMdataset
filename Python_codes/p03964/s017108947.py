a=b=1
for _ in range(int(input())):
  c,d=map(int,input().split())
  m=max(0--a//c,0--b//d)
  a,b=c*m,d*m
print(a+b)