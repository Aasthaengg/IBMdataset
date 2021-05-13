a, b, c = map(int, input().split())
ab = a + b
ac = a + c
bc = b + c

if ab == c:
    print('Yes')
elif ac == b:
    print('Yes')
elif bc == a:
    print('Yes')
else:
    print('No')