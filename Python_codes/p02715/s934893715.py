n, k = map(int, input().split())

m = 10**9+7

def f(n, k):
  res = 0
  lst = [0]*(k+1)
  for i in range(k, 0, -1):
    lst[i] = pow((k//i), n, m) - sum(lst[i*j] for j in range(2, k//i+1))%m
    res += i*lst[i]
    res %= m
  return res

print(f(n, k))