
N, W = map(int, input().split())
w, v = [0]*N, [0]*N
for i in range(N):
    w[i], v[i] = map(int, input().split())

memo = {}

def knapsack(i, j):
    key = '{}-{}'.format(i, j)
    if key in memo:
        return memo[key]
    if i == N:
        r = 0
    elif j < w[i]:
        r = knapsack(i + 1, j)
    else:
        r = max([knapsack(i + 1, j), knapsack(i + 1, j - w[i]) + v[i]])
    memo[key] = r
    return r

print(knapsack(0, W))
