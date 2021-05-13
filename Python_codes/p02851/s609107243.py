n,k = map(int, input().split())
a = [0] + list(map(int, input().split()))
for i in range(n):
    a[i+1] = (a[i] + a[i+1]-1)%k
d = dict()
ans = 0
for i in range(n+1):
    if i >= k:
        d[a[i-k]] -= 1
    if a[i] in d:
        ans += d[a[i]]
        d[a[i]] += 1
    else:
        d[a[i]] = 1
print(ans)
