m, k = map(int, input().split())
if m == 1:
    if k == 0:
        print('0 0 1 1')
    else:
        print(-1)
else:
    if k < 2 ** m:
        for i in range(2 ** m):
            if i != k:
                print(i, end = ' ')
        print(k, end = ' ')
        for i in reversed(range(2 ** m)):
            if i != k:
                print(i, end = ' ')
        print(k)
    else:
        print(-1)