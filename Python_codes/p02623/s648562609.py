def bs(k, m):
    i = -1
    pas = 1<<30
    while pas:
        if i+pas < m and u[i+pas] <= k:
            i += pas
        pas //= 2
    return i+1

n, m, k = map(int, input().split())
v = list(map(int, input().split()))
u = list(map(int, input().split()))
for i in range(1, n):
    v[i] += v[i-1]
for i in range(1, m):
    u[i] += u[i-1]
ans = bs(k, m)
for i in range(n):
    if v[i] <= k:
        ans = max(ans, bs(k-v[i], m) + i+1)
print(ans)