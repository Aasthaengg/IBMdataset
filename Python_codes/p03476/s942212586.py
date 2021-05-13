Q = int(input())

p = [True] * (10 ** 5 + 1)
p[0] = p[1] = False
for i in range(2, 10 ** 5 + 1):
    for j in range(2 * i, 10 ** 5 + 1, i):
        p[j] = False

pp = [0] * (10 ** 5 + 1)
for i in range(1, 10 ** 5 + 1):
    pp[i] = int(p[i] and p[(i + 1) // 2]) + pp[i - 1]

res = 0
for _ in range(Q):
    l, r = map(int, input().split())
    print(pp[r] - pp[l - 1])
