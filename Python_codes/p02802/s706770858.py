n, m = map(int, input().split())
ps = [list(input().split()) for _ in range(m)]
ac = [0]*n
wa = [0]*n
cnt = [0]*n
for i in range(m):
    x = int(ps[i][0]) - 1
    if ps[i][1] == "AC" and ac[x] == 0:
        ac[x] = 1
        wa[x] = cnt[x]
    elif ps[i][1] == "WA" and ac[x] == 0:
        cnt[x] += 1
print(sum(ac), sum(wa))