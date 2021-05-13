M, K = map(int, input().split())
if K >= 2**M:
    print(-1)
elif M == 1:
    if K == 0:
        print(0, 0, 1, 1)
    else:
        print(-1)
else:
    A = list(range(K)) + list(range(K+1,2**M))
    print(" ".join(map(str,A+[K]+A[::-1]+[K])))