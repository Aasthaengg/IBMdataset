t1, t2 = map(int, input().split())
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

if t1 * a1 + t2 * a2 == t1 * b1 + t2 * b2:
    print("infinity")
    exit(0)
if t1 * a1 + t2 * a2 > t1 * b1 + t2 * b2:
    a1, b1 = b1, a1
    a2, b2 = b2, a2
if a1 < b1:
    print("0")
    exit(0)

l, r, labe, ans = 2, 10**18, False, 10**18

while l <= r:
    m = l + (r - l) // 2
    xa = (m - 1) * (t1 * a1 + t2 * a2) + t1 * a1
    xb = (m - 1) * (t1 * b1 + t2 * b2) + t1 * b1
    if xa == xb:
        labe = True
        ans = m
        break;
    elif xa < xb:
        ans = m
        r = m - 1
    else :
        l = m + 1

if labe:
    print(2 * (ans - 1))
else :
    print(2 * (ans - 1) - 1)

