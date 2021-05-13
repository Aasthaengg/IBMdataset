n=int(input())
sm=0
for i in range(1,n+1):
  if (i % 3)*(i%5)>0:
    sm+=i
print(sm)