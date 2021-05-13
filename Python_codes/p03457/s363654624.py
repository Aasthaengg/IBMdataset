N = int(input())

xyz = [map(int, input().split()) for i in range(N)]
t, x, y = [list(i) for i in zip(*xyz)]



if N == 1:
    T = N
    SUM = abs(x[0] + y[0])
    if T < SUM:
        print('No')
        exit()
    elif (T % 2 == 0 and SUM % 2 != 0) or (T % 2 != 0 and SUM % 2 == 0):
        print('No')
        exit()
    else:
        print('Yes')
        exit()
    

for i in range(N-1):
    T = t[i+1] - t[i]
    X = x[i+1] - x[i]
    Y = y[i+1] - y[i]
    

    
    
    if t[0] < abs(x[0] + y[0]):
        print('No')
        exit()
    elif (t[0] % 2 == 0 and abs((x[0] + y[0])) % 2 != 0) or (t[0] % 2 != 0 and abs((x[0] + y[0])) % 2 == 0):
        print('No')
        exit()
    

    SUM = abs(X + Y)

    if T < SUM:
        print('No')
        exit()
    elif (T % 2 == 0 and SUM % 2 != 0) or (T % 2 != 0 and SUM % 2 == 0):
        print('No')
        exit()
    else:
        continue
    
print('Yes')