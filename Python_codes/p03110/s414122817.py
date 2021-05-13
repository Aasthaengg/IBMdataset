n=int(input())
sm=0
for i in range(n):
  x,y=map(str,input().split())
  if y=='JPY':
    sm+=int(x)
  else:
    sm+=float(x)*380000.0
print(sm)