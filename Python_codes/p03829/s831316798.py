N, A, B = map(int, input().split())
X = list(map(int, input().split()))

sa_cost = [0] * (N - 1)
for i in range(N - 1):
    sa_cost[i] = (X[i + 1] - X[i]) * A


ans = 0
for i in range(len(sa_cost)):
    if sa_cost[i] <= B:
        ans += sa_cost[i]
    else:
        ans += B

print(ans)
