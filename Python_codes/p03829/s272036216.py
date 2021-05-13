N, A, B = map(int, input().split())
X = list(map(int, input().split()))

diffs = []
for i in range(len(X) - 1):
    left, right = X[i], X[i + 1]
    diffs.append(right - left)
costs = []
for diff in diffs:
    costs.append(min(diff * A, B))
print(sum(costs))
