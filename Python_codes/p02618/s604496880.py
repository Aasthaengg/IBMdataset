d = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for _ in range(d)]
k = [-1] * 26
for i in range(d):
    res = -100000000
    p = 0
    for j in range(26):
        tmp = 0
        tmp += s[i][j]
        for x in range(26):
            if x == j:
                continue
            tmp -= c[x] * (i - k[x] + 6)
        if res < tmp:
            res = tmp
            p = j
    k[p] = i
    print(p + 1)
