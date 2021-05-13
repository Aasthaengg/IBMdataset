MAX = 10 ** 5 + 1
f = [True] * (MAX)
c = [0] * (MAX + 1)
for i in range(2, MAX):
    if f[i]:
        for j in range(i + i, MAX, i):
            f[j] = False
for i in range(3, MAX, 2):
    if f[i] and f[(i + 1) // 2]:
        c[i] += 1
for i in range(3, MAX):
    c[i] += c[i - 1]

Q = int(input())
for i in range(Q):
    l, r = map(int, input().split())
    print(c[r] - c[l - 1])

