a, b, c = (int(x) for x in input().split())
if a + b == c or b + c == a or c + a == b:
    print('Yes')
else:
    print('No')