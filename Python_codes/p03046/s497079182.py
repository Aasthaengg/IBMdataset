M, K = map(int, input().split())
maxim = 2 ** M

if maxim <= K:
    print("-1")
else:
    if maxim == 1 and K == 0:
        print("0 0")
    elif maxim == 2:
        if K == 0:
            print("0 0 1 1")
        elif K == 1:
            print("-1")
    else:
        for i in range(maxim):
            if i != K:
                print(str(i), end=" ")
        print(str(K), end=" ")
        for i in range(maxim - 1, -1, -1):
            if i != K:
                print(str(i), end=" ")
        print(str(K))
