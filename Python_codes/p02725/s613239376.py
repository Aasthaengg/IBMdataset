k, n = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

dists = list()
dists.append(a[0] - a[-1] + k)
for i in range(1, n):
    dists.append(abs(a[i] - a[(i - 1)]))
print(k - max(dists))
