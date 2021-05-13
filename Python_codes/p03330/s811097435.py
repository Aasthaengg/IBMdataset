import sys
input = sys.stdin.readline

n, c = [int(x) for x in input().split()]

d_list = [[int(x) for x in input().split()] for _ in range(c)]
c_ = [[int(x) for x in input().split()] for _ in range(n)]

mod_0 = [0] * c
mod_1 = [0] * c
mod_2 = [0] * c

for i in range(n):
    for j in range(n):
        if (i + j) % 3 == 0:
            m = mod_0
        elif (i + j) % 3 == 1:
            m = mod_1
        else:
            m = mod_2
        for k in range(c):
            m[k] += d_list[c_[i][j] - 1][k]

ans = 10 ** 18

for i in range(c):
    for j in range(i + 1, c):
        for k in range(j + 1, c):
            a = mod_0[i] + mod_1[j] + mod_2[k]
            b = mod_0[i] + mod_1[k] + mod_2[j]
            c__ = mod_0[j] + mod_1[i] + mod_2[k]
            d = mod_0[j] + mod_1[k] + mod_2[i]
            e = mod_0[k] + mod_1[i] + mod_2[j]
            f = mod_0[k] + mod_1[j] + mod_2[i]
            ans = min(ans, a, b, c__, d, e, f)

print(ans)