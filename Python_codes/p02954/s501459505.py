s = input()

l = []
tmp = 0
d = 'R'
for x in s:
    if x == d:
        tmp += 1
    else:
        l.append(tmp)
        tmp = 1
        d = x
else:
    l.append(tmp)
res = []
for i in range(0, len(l), 2):
    a, b = l[i:i+2]
    c = a + b
    if c % 2 == 0:
        p = q = c // 2
    else:
        p, q = c // 2 + 1, c // 2
        if (a > b and a % 2 == 0) or (a < b and b % 2 == 1):
            p, q = q, p

    res += [0] * (a-1) + [p] + [q] + [0] * (b-1)

print(*res)
