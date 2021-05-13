N = int(input())
divisors = [0 for _ in range(N+1)]
result = 0

for n in range(1, N+1):
  for m in range(n, N+1, n):
    divisors[m] += 1
for i, d in enumerate(divisors):
  result += i * d
print(result)
