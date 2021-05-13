n = int(input())

robots = []
for i in range(n):
    x, l = map(int, input().split())
    robots.append([x + l, x - l])

robots.sort()

ans = n
n_r = robots[0][0]
for i in range(1, n):
    r = robots[i][0]
    l = robots[i][1]
    if n_r > l:
        ans -= 1
    else:
        n_r = r

print(ans)
