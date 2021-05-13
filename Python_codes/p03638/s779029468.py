h, w = map(int, input().split())
n = int(input())
a = [int(i) for i in input().split()]
c = [[0] * w for _ in range(h)]
i, j = 0, 0
d = 1
k = 1
for ai in a:
    for _ in range(ai):
        c[j][i] = k
        if i == 0 and d == -1:
            j += 1
            d = 1
        elif i == w - 1 and d == 1:
            j += 1
            d = -1
        else:
            i += d
    k += 1
[print(*e) for e in c]