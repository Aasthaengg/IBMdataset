N, M = map(int, input().split())
count = [0]*N
ans = 0
ok = 0
for _ in range(M):
    p, s = input().split()
    if count[int(p)-1] >= 0 and s == "WA":
        count[int(p) - 1] += 1
    elif count[int(p)-1] >= 0 and s == "AC":
        ans += count[int(p)-1]
        count[int(p)-1] = -1
        ok += 1
print(ok, ans)