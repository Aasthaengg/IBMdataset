n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

l = [i for i in range(n)]
pos = [0] * n
res = 0
cnt = 0
while True:
    res += 1
    flag = True
    tmp = l.copy()
    l = []
    used = [False] * n
    for v in tmp:
        if used[v] or pos[v] == n - 1:
            continue

        opp = a[v][pos[v]] - 1

        if used[opp] or pos[opp] == n - 1:
            continue

        if a[opp][pos[opp]] - 1 == v:
            pos[v] += 1
            pos[opp] += 1
            l.append(v)
            l.append(opp)
            used[v] = True
            used[opp] = True
            flag = False
            if pos[v] == n - 1:
                cnt += 1
            if pos[opp] == n - 1:
                cnt += 1

    if flag:
        print(-1)
        break

    if cnt == n:
        print(res)
        break