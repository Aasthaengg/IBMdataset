n = int(input())
A = tuple(map(int, input().split()))

d = dict()
for a in A:
    d.setdefault(a, 0)
    d[a] += 1

c = 0
for i, count in d.items():
    rem = count - i
    if rem < 0:
        c += count
    else:
        c += rem
print(c)
