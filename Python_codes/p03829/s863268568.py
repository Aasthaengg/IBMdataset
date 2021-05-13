n, a, b = map(int, input().split())
ns = list(map(int, input().split()))
dis = [ns[i + 1] - ns[i] for i in range(n - 1)]
ttl = 0
for i in range(0, n-1):
    ttl += min(dis[i] * a, b)
print(ttl)