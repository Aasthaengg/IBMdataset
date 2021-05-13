n, c = map(int, input().split())
stc = [list(map(int, input().split())) for _ in range(n)]
T = 10**5+1
record = [[0]*(T+3) for _ in range(c+1)]
channel = [[] for _ in range(c+1)]
stc.sort()

for s, t, c in stc:
    if not channel[c]:
        channel[c].append([s - 1, t])
        continue
    if channel[c][-1][1] == s:
        channel[c][-1][1] = t
    else:
        channel[c].append([s-1, t])

for i, v in enumerate(channel):
    for s, t in v:
        record[i][s] += 1
        record[i][t] -= 1

for i in record:
    for j in range(T+2):
        i[j+1] += i[j]

ans = 0
for i in range(T+2):
    y = 0
    for r in record:
        y += r[i]
    ans = max(ans, y)
print(ans)