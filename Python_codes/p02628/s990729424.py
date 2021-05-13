N, K = input().split()
N, K = int(N), int(K)
p = list(map(int, input().split()))
sum = 0
for i in range(K):
  min_price = min(p)
  p.remove(min(p))
  sum+= min_price
print(sum)
