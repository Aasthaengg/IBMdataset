M, K = map(int, input().split())

if K >= 2**M:
    anss = []
else:
    if M == 0:
        anss = [0,0]
    elif M == 1:
        if K == 0:
            anss = [0,0,1,1]
        else:
            anss = []
    else:
        Bs = [i for i in range(2**M) if i != K]
        anss = Bs+[K]+Bs[::-1]+[K]

if not anss:
    print(-1)
else:
    print(' '.join(map(str, anss)))
