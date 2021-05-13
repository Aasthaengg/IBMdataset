n, m = map(int, input().split())
a = [0]*m
for _ in range(n):
    k = list(map(int, input().split()))
    for i in range(m):
        if i+1 in k[1:]:
            a[i] += 1
ans = 0
for i in range(m):
    if a[i] == n:
        ans += 1
print(ans)
