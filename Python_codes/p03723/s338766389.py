a,b,c = map(int, input().split())
val = 0
if a == b == c and a%2 == 0 and b%2 == 0 and c%2 == 0:
  print(-1)
else:
  while a%2 == 0 and b%2 == 0 and c%2 == 0:
    a,b,c = int((b+c)/2), int((a+c)/2), int((a+b)/2)
    val += 1
  print(val)