m, k = map(int, input().split())

if m == 1:
    if k == 0:
        print("0 0 1 1")
    else:
        print(-1)
else:
    if 2**m <= k:
        print(-1)
    else:
        ANS = []
        for i in range(2**m):
            if i != k:
                ANS.append(i)
        ANS.append(k)
        for i in range(2**m-1,-1,-1):
            if i != k:
                ANS.append(i)
        ANS.append(k)
        print(*ANS)