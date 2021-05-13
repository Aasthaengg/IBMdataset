# C Peaks

N, M = map(int, input().split())
H = list(map(int, input().split()))

goods = [0] * N
for i in range(M):
  a, b = map(int, input().split())
  if H[a-1] > H[b-1]:
    goods[b-1] = 1
  elif H[a-1] < H[b-1]:
    goods[a-1] = 1
  elif H[a-1] == H[b-1]:
    goods[a-1] = 1
    goods[b-1] = 1

print(goods.count(0))