N = int(input())
K = int(input())
result = 1

for i in range(N):
  if result*2 >= result+K:
    result += K
  else:
    result *= 2

print(result)