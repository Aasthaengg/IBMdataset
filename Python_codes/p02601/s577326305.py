a,b,c = map(int,input().split())
k = int(input())

for _ in range(k):
  if a >= b:
    b *= 2
  elif b >= c:
    c *= 2
  else:
    break
if c > b > a:
  print("Yes")
else:
  print("No")