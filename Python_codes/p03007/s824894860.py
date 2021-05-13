n = int(input())
a = list(map(int, input().split()))
plus, minus = [], []
for x in a:
    if x < 0: minus.append(x)
    else: plus.append(x)

if plus and minus:
    print(sum(map(abs, a)))
    p = plus[0]
    for x in minus[1:]:
        print(p, x)
        p -= x
    
    m = minus[0]
    for x in plus[1:]:
        print(m, x)
        m -= x
    
    print(p, m)

if not plus:
    minus.sort(reverse=True)
    m = minus[0]
    print(-(sum(minus) - m * 2))
    for x in minus[1:]:
        print(m, x)
        m -= x

if not minus:
    plus.sort()
    p = plus[0]
    print(sum(plus) - p * 2)
    for x in plus[2:]:
        print(p, x)
        p -= x
    print(plus[1], p)
