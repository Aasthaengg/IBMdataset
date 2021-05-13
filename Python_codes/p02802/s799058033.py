n, m = map(int, input().split())
a = [input().split() for i in range(m)]

solved = [False] * n
ac_cnt = 0
wa_l = [0] * n

for i in range(m):
    cn, cj = int(a[i][0]) - 1, a[i][1]
    if not solved[cn]:
        if cj == 'WA':
            wa_l[cn] += 1
        else:
            ac_cnt += 1
            solved[cn] = True
wa_cnt = 0
for i in range(n):
    wa_cnt += solved[i] * wa_l[i]
print(ac_cnt, wa_cnt)
