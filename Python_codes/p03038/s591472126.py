n, m = map(int, input().split())
A = list(map(int, input().split()))
d = {}
for a in A:
    d[a] = 1 if a not in d else d[a] + 1
for _ in range(m):
    b, c = map(int, input().split())
    d[c] = b if c not in d else d[c] + b
ans = 0
cnt = 0
L = sorted(d, reverse=True)
for k in L:
    if d[k] + cnt < n:
        ans += k * d[k]
        cnt += d[k]
    else:
        ans += k * (n - cnt)
        break
print(ans)
