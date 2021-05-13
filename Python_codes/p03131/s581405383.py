K,A,B = map(int, input().split())
if B - A < 3:
    print(1+K)
else:
    if K - (A-1) < 2:
        print(1+K)
    else:
        K -= A-1
        if K%2 == 0:
            print((B-A)*K//2 + A)
        else:
            print((B-A)*(K-1)//2 + A + 1)