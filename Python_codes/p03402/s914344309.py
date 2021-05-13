A, B = map(int, input().split())
if A <= B:
    s0, s1 = '.', '#'
    M, m = B, A
else:
    s0, s1 = '#', '.'
    M, m = A, B

print(100, 100)

ans = [[s0] * 100 for _ in range(100)]
ans[0] = [s1] * 100
ans[1] = [s0, s1] * 50
M -= 1
m -= 1

y, x = 2, 0
for _ in range(m):
    ans[y][x] = s1
    x += 2
    if x >= 100:
        y += 1
        x = y % 2
y, x = 98, 1
for _ in range(M - m):
    ans[y][x] = s1
    x += 2
    if x >= 100:
        y -= 2
        x = 1
for a in ans:
    print(''.join(map(str, a)))

