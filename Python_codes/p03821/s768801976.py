n = int(input())
ans = 0

a, b = [], []
for i in range(n):
    ai, bi = map(int, input().split())

    a.append(ai)
    b.append(bi)

c = 0
for i in reversed(range(n)):
    a[i] += c
    x = a[i] % b[i]
    if x:
        if a[i] < b[i]:
            c += b[i] - a[i]
        elif a[i] > b[i]:
            c += b[i] - x

print(c)
