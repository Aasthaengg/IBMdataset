a, b, d = [], [], []
amount = 0
for i, x in enumerate(input()):
    if x == '\\':
        a += [i]
    elif x == '/' and a:
        j = a.pop()
        pool = i - j
        amount += pool
        while b and b[-1] > j:
            pool += d.pop()
            b.pop()
        b.append(j)
        d.append(pool)
print(amount)
print(len(b), *d)
