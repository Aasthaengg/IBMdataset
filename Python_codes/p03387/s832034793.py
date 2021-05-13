def f(abc,c):
    m = max(abc)
    a = 0
    for i in abc:
        a += (i < m)
    if a == 0:
        return c
    c += 1
    if a <= 1:
        for i,x in enumerate(abc):
            if x < m:
                abc[i] += 2
                break
        return f(abc,c)
    else:
        for i,x in enumerate(abc):
            if x < m:
                abc[i] += 1
        return f(abc,c)


abc = list(map(int, input().split()))
print(f(abc,0))
