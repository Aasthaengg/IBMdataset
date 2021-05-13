N,K = map(int, input().split())
total = 0
p = [int(i) for i in input().split()]
for j in range(K):
  p.sort()
  total += p[j]
print(total)