def f(i):
    global m
    if i == n:
        c = 1
        for j in s:
            if j == 0:
                c *= 2
            else:
                c += k
        if m > c:
            m = c
        return
    f(i + 1)
    s[i] = 1
    f(i + 1)
    s[i] = 0

n = int(input())
k = int(input())
s = [0] * n
m = 114514
f(0)
print(m)