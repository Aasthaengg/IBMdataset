X, N = map(int, input().split())
if int(N) == 0:
    print(X)
else:
    Y = list(map(int, input().split()))
    x = int(X)
    for i in range(100):
        if x - i not in Y:
            print(x - i)
            break
        elif x + i not in Y:
            print(x + i)
            break
