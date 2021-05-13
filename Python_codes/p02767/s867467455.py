N = int(input())
X = list(map(int, input().split()))

costs = []
for p in range(100):
  costs.append(sum(map(lambda x: (x - p)**2, X)))

print(min(costs))