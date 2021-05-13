def f(i):
    global ans
    if i == n:
        w, x, y, z = 0, 0, 0, 0
        for i in range(n):
            if s[i] == 1:
                x += l[i]
            elif s[i] == 2:
                y += l[i]
            elif s[i] == 3:
                z += l[i]
            else:
                w += 1
        if x > 0 and y > 0 and z > 0:
            mp = abs(a - x) + abs(b - y) + abs(c - z) + 10 * (n - w - 3)
            ans = min(ans, mp)
        return
    s[i] = 0
    f(i + 1)
    s[i] = 1
    f(i + 1)
    s[i] = 2
    f(i + 1)
    s[i] = 3
    f(i + 1)

n, a, b, c = map(int, input().split())
l = [int(input()) for _ in range(n)]
s = [3] * n
ans = 114514
f(0)
print(ans)