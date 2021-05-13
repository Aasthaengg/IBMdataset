t1, t2 = map(int,input().split())
a1, a2 = map(int,input().split())
b1, b2 = map(int,input().split())

c1 = a1 * t1
c2 = a2 * t2
d1 = b1 * t1
d2 = b2 * t2

if c1 + c2 == d1 + d2:
    print("infinity")
    exit(0)

if c1 + c2 < d1 + d2:
    c1, d1 = d1, c1
    c2, d2 = d2, c2

# print(c1, c2, d1, d2)

def check(mid):
    if mid % 2 == 0:
        a = (c1 + c2) * (mid // 2)
        b = (d1 + d2) * (mid // 2)
        f1 = a < b
        a += c1
        b += d1
        if a == b:
            return True
        f2 = a < b
        return f1 != f2
    else:
        a = (c1 + c2) * (mid // 2) + c1
        b = (d1 + d2) * (mid // 2) + d1
        f1 = a < b
        a += c2
        b += d2
        if a == b:
            return True
        f2 = a < b
        return f1 != f2

ok, ng = 0, 10 ** 20
while ng - ok > 1:
    mid = (ok + ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)