A, B = map(int, input().split())

ans = [[None for _ in range(100)] for _ in range(100)]
for i in range(100):
    for j in range(100):
        ans[i][j] = '#' if i < 50 else '.'

A -= 1
B -= 1

i, j = 0, 0
while A > 0:
    ans[i][j] = '.'
    A -= 1

    j += 2
    if j >= 100:
        j = 0
        i += 2

i, j = 51, 0
while B > 0:
    ans[i][j] = '#'
    B -= 1

    j += 2
    if j >= 100:
        j = 0
        i += 2

print(100, 100)
for i in range(100):
    print(*ans[i], sep='')
