x = int(input())
while True:
  c = 0
  for i in range(2, x):
    if x % i == 0:
      c += 1
      continue
  if c == 0:
    break
  
  x += 1
  
print(x)