K, T = map(int, input().split())
a = list(map(int, input().split()))

if T == 1:
    print(K - 1)
else:
    M = max(a)
    rest = sum(a) - M

    if rest >= M - 1:
        print(0)
    else:
        print(M - rest - 1)
