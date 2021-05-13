n = int(input())
 
s = 0
p = 0
for _ in range(n):
  t,x,y = map(int, input().split())
  s = t - s
  p = abs((x+y)-p)
  if s < p:
    print("No")
    exit()
  elif s%2 != p%2:
    print("No")
    exit()
print("Yes")