a, b, c, d = (int(x) for x in input().split())
dis1 = abs(a-b)
dis2 = abs(b-c)
dis3 = abs(a-c)
if dis3 <= d or (dis1 <= d and dis2 <= d):
    print('Yes')
else:
    print('No')