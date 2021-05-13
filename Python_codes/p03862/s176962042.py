N, X = map(int, input().split(' '))
A = list(map(int, input().split(' ')))

cost = 0
diff = max(0, sum(A[0:2]) - X)
A[0] -= max(0, diff - A[1])
A[1] -= min(A[1], diff)
cost += diff

for i in range(2, N):
    diff = max(0, A[i - 1] + A[i] - X)
    A[i - 1] -= max(0, diff - A[i])
    A[i] -= min(A[i], diff)
    cost += diff

print(cost)
