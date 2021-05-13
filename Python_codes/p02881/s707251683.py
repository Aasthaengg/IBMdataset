N = int(input())
# 99分解して、マンハッタン距離を求める
# ただし、iとjが近い方が距離が短くなる

cand = 1
n = 1
while n * n <= N:
  if N % n == 0:
    cand = n
  n += 1

print(cand - 1 + N // cand - 1)