N, X, T = map(int, input().split())
result = N // X * T
if N % X > 0:
  result += T
print(result)