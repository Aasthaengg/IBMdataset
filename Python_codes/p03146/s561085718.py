s = int(input())


def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


p = {s: 1}
m = 1
while True:
    s = f(s)
    m += 1
    if s in p:
        print(m)
        break
    else:
        p[s] = m
