a, b, c, d = map(int, input().split())

x1 = abs(a - b)
x2 = abs(b - c)
ac = abs(a - c)

if ac <= d:
    print('Yes')
elif (x1 <= d) and (x2 <= d):
    print('Yes')
else:
    print('No')
