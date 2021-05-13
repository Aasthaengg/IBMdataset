def f(n):
    return 3 * n + 1 if n % 2 else n // 2


a = int(input())
i = 1
s = set([a])
while True:
    i += 1
    a = f(a)
    if a in s:
        break
    s.add(a)

print(i)