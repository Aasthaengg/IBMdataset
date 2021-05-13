(n, m, q) = map(int, input().split())
num_sets = [tuple(map(int, input().split())) for _ in range(q)]

a_opt = []
for ni in range(n):
    a_opt_next = []
    if len(a_opt) == 0:
        for mi in range(1, m + 1):
            a_next = [mi]
            a_opt_next.append(a_next)
    else:
        for a in a_opt:
            for mi in range(a[-1], m + 1):
                a_next = a + [mi]
                a_opt_next.append(a_next)
    a_opt = a_opt_next[:]

ans = 0
for a in a_opt:
    sumd = 0
    for num_set in num_sets:
        if a[num_set[1] - 1] - a[num_set[0] - 1] == num_set[2]:
            sumd += num_set[3]
    ans = max(ans, sumd)

print(ans)
