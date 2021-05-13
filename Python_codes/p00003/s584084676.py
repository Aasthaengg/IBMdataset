def isRTri(a, b, c):
    return a * a + b * b == c * c

a = [0, 0, 0]
n = input()
for k in range(n):
    a = map(int, raw_input().split())
    a.sort()
    r = isRTri(a[0], a[1], a[2])
    print "YES" if r else "NO"