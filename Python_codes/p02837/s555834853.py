n = int(input())
a, xy = [], []
for _ in range(n):
    a_t = int(input())
    xy_t = [list(map(int, input().split())) for _ in range(a_t)]
    a.append(a_t)
    xy.append(xy_t)

ans = 0
for i in range(2**n):
    flag = True
    for j in range(n):
        if (i >> j) & 1:
            for k in xy[j]:
                if (i >> (k[0]-1)) & 1 != k[1]:
                    flag = False
                    break
    if flag:
        ans = max(ans, bin(i).count('1'))
print(ans)