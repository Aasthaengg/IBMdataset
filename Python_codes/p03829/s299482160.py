N, A, B = map(int, input().split())
X = list(map(int, input().split()))

res = 0
for i in range(1, N):
    w = (X[i] - X[i - 1]) * A
    t = B
    res += min(w, t)

print(res)
