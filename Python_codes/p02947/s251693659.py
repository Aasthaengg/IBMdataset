N = int(input())
d = {}
ans = 0
for i in range(N):
    t = str(sorted(input()))
    if (d.get(t, "Not") == "Not"):
        d[t] = 1
    else:
        ans += d[t]
        d[t] += 1
print(ans)
