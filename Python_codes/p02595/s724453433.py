import math
n,d = map(int,input().split())
c = 0

for i in range (n):
  a,b = map(int,input().split())
  if math.sqrt(a*a +b*b) <=d:
    c+=1

print(c)
