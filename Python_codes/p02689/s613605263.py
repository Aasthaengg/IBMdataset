n, m = map(int, input().split())
h = list(map(int, input().split()))
mh = [0] * n
for i in range(m):
    a, b = map(int, input().split())
    mh[a - 1] = max(mh[a - 1], h[b - 1])
    mh[b - 1] = max(mh[b - 1], h[a - 1])
print(sum(h[i] > mh[i] for i in range(n)))