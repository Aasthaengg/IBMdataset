def resolve():
    input()
    L = list(map(int, input().split()))
    M = max(L)
    R = sum(L) - M
    if R > M:
        print('Yes')
    else:
        print('No')
resolve()        