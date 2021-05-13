memo = {}

def fib_memo(n):
  if n <= 1:
    return 1
  if n in memo:
    return memo[n]
  memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
  return memo[n]

x = int(raw_input())

print fib_memo(x)