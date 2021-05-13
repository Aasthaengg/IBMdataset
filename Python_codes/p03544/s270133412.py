memo = {0:2, 1:1}
def f(n):
  global memo
  if n in memo:
    return memo[n]
  else:
    res = f(n-1) + f(n-2)
    memo[n] = res
    return res

print(f(int(input())))