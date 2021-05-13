n, k = map(int, input().split())
h = list(sorted(map(int, input().split()))[::-1])
i = 0
for j in range(n):
    if h[j] >= k:
        i += 1
print(int(i))