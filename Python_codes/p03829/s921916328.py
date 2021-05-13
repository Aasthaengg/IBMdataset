N, A, B = map(int, input().split())
X = [int(_) for _ in input().split()]

diff = [X[n + 1] - X[n] for n in range(N - 1)]

ans = 0
for n in range(N - 1):
    if diff[n] * A > B:
        ans += B
    else:
        ans += diff[n] * A
print(ans)