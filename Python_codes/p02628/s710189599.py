N, K = map(int, input().split())
p = list(map(int, input().split()))

p = sorted(p)
price = 0
for i in range(K):
  price += p[i]
print(price)