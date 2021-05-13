n, m = map(int, input().split())
l1 = [list(map(int, input().split())) for _ in range(n)]
l2 = [list(map(int, input().split())) for _ in range(m)]

for a, b in l1:
    res_d = float('inf')
    res_n = 0
    for i in range(m):
        c, d = l2[i]
        if res_d > abs(a - c) + abs(b - d):
            res_d = abs(a - c) + abs(b - d)
            res_n = i + 1
    print(res_n)