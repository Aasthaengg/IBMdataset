n, k = map(int, input().split())
hh = []
minn = 10**12
for i in range(n):
    h = int(input())
    hh.append(h)
h = sorted(hh)
for i in range(n - k + 1):
    if h[i + k - 1] - h[i] < minn:
        minn = h[i + k - 1] - h[i]
print(minn)
