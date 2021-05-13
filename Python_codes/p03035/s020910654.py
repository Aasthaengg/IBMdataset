a,b = map(int,input().split())
cost = 0

if a >= 13:
  cost = b
if a >= 6 and a <= 12:
  cost = int(b / 2)
  
print(cost)