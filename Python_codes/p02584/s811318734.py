def solve():
  X, K, D = map(int, input().split())
  X = abs(X)
  if X>=K*D:
    return X-K*D
  X -= D*(K%2)
  r =  X%(D*2)
  return min(r,2*D-r)
print(solve())