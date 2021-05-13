X = int(input())

if X == 1:
  print(1)
  exit()

ans = 0

for b in range(2, int(X**0.5)+2):
  temp = b
  while temp <= X:
    ans = max(ans, temp)
    temp *= b

print(ans)