a, b, c = map(int, input().split())

if a != 1 and a == b == c:
  print(-1)
  exit()
  
result = 0

while True:
  if any([a & 1, b & 1, c & 1]):
    break
    
  a2 = a // 2
  b2 = b // 2
  c2 = c // 2
  a = b2 + c2
  b = a2 + c2
  c = a2 + b2
  result += 1

print(result)