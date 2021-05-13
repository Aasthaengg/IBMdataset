N = int(input())
T = list(map(int, input().split()))
M = int(input())
px = [tuple(map(int, input().split())) for _ in range(M)]
ans = sum(T)
for p, x in px:
  print(ans - (T[p - 1] - x))