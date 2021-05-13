a, b, c = map(int, input().split())
res = c - b - a
if res > 0 and res*res - 4*a*b > 0:
    print('Yes')
else:
    print('No')