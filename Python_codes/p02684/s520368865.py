n, k = map(int, input().split())
a = list(map(lambda x: int(x) - 1, input().split()))

tel = [[0] * n for _ in range(63)]
tel[0] = a
for i in range(62):
    for j in range(n):
        tel[i + 1][j] = tel[i][tel[i][j]]

now = 0
for i in range(62, -1, -1):
    if k >> i & 1:
        now = tel[i][now]
print(now + 1)
