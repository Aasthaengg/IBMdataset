N, M = map(int, input().split())

Z = []
for i in range(N):
  a, b = map(int, input().split())
  Z.append((a, b))

Z.sort(key=lambda x:x[0])

count = 0
cost = 0
shop = 0
while count < M:
  buy = min(Z[shop][1], M - count)
  count += buy
  cost +=  buy * Z[shop][0]
  if count < M:
    shop += 1
  
print(cost)