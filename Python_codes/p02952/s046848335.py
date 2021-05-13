n = int(input())
c = 0

while True:
  if n == 0:
    break
  else:
    x = len(str(n))
    if x%2 == 1:
      c += 1
  n -= 1
  
print(c)