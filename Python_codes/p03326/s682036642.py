def f(i):
    global ans
    if i == 3:
        l = []
        for j in range(n):
            c = 0
            for k in range(3):
                c += t[k] * s[j][k]
            l.append(c)
        l.sort(reverse = True)
        d = 0
        for j in range(m):
            d += l[j]
        if d > ans:
            ans = d
        return
    f(i + 1)
    t[i] = 1
    f(i + 1)
    t[i] = -1

n, m = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]
t = [-1] * 3
ans = 0
f(0)
print(ans)