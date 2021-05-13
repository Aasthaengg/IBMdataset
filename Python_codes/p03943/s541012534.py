X = [int(x) for x in input().split()]
Y = sorted(X)
if Y[0] + Y[1] == Y[2]:
    print('Yes')
else:
    print('No')