N, K = map(int, input().split())

p = list(map(int, input().split()))

p.sort()
cost = 0

for k in range(K):
    cost += p[k]
print(cost)