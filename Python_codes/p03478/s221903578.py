n, a, b = map(int, input().split())
 
total = 0
for i in range(n+1):
  x = str(i)
  y = 0
  for j in x:
    y += int(j)
  if a <= y <= b:
    total += i
print(total)