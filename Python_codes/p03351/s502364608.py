a, b, c, d = map(int, input().split())
ab = abs(b - a)
bc = abs(c - b)
ac = abs(c - a)
if ab <= d and bc <= d:
    print('Yes')
elif ac <= d:
    print('Yes')
else:
    print('No')