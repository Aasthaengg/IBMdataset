n, m = map(int, input().split())
K = [list(map(int, input().split())) for _ in range(m)]
P = list(map(int, input().split()))
ans = 0
for i in range(2**n):
    flag = [False] * n
    for j in range(n):
        if (i >> j) & 1:
            flag[j] = True
    on = [False] * m
    for j in range(m):
        sw = 0
        for k in range(1, K[j][0] + 1):
            if flag[K[j][k] - 1]:
                sw += 1
        if sw % 2 == P[j]:
            on[j] = True
    if False not in on:
        ans += 1
print(ans)