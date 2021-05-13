a, b, c, d = [int(x) for x in input().split()]

if (abs((a - b)) <= d) and (abs((c - b)) <= d) or abs(c-a) <=d :
    print('Yes')
else:
    print('No')
