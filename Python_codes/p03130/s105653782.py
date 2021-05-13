a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
a3, b3 = map(int, input().split())
ab = [a1, a2, a3, b1, b2, b3]

if ab.count(1) >= 3 or ab.count(2) >= 3 or ab.count(3) >= 3 or ab.count(4) >= 3:
    print('NO')
else:
    print('YES')
