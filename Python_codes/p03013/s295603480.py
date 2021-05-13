n, m = map(int, input().split())

memo = [-1] * (n + 1)
memo[0] = 1
memo[1] = 1
for i in range(m):
  memo[int(input())] = 0

def fib(x):
  if memo[x] == -1:
    memo[x] = fib(x-1) + fib(x-2)
  return memo[x]

def fib2(x):
  if x <= 1:
    return memo[x]
  else:
    for i in range(x - 1):
      if memo[i + 2] == 0:
        continue
      memo[i + 2] = memo[i] + memo[i + 1]
    return memo[x]

# print(fib2(n))
# print(memo)
print(fib2(n) % 1000000007)
