N = int(input())
d = {}
ans = 0
for _ in range(N):
    s = str(sorted(input()))
    if s not in d.keys():
        d[s] = 0
    else:
        d[s] += 1
        ans += d[s]
print(ans)
