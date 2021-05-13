N, Y = map(int, input().split())

checker = Y // 1000
ans = [-1, -1, -1]
for x in range(N + 1):
    for y in range(N + 1):
        z = N - x - y
        if z < 0:
            break
        if (x + 5 * y + 10 * z) == checker:
            ans = [z, y, x]
            break
print('{} {} {}'.format(ans[0], ans[1], ans[2]))