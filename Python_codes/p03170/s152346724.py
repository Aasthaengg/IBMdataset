def solve():
    N, K = map(int, input().split())
    As = list(map(int, input().split()))

    WLs = [0] * (K+1)
    for x in range(1, K+1):
        for A in As:
            if x-A < 0:
                break
            if WLs[x-A] == 0:
                WLs[x] = 1
                break

    if WLs[K]:
        print('First')
    else:
        print('Second')


solve()

