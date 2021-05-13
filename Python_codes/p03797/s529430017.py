N, M = list(map(int,input().split()))

x = M - 2 * N
if x > 0:
  N += x // 4

print(min(N, M // 2))