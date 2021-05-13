n = int(input())
A = list(map(int, input().split()))

ANS = []
B=A[:]
B.sort()

if abs(B[0]) > abs(B[-1]) :
    absmax = B[0]
else :
    absmax = B[-1]

ind = A.index(absmax)

if absmax != 0 :
    fugou = absmax // abs(absmax)

    for i in range(n) :
        if A[i] * fugou < 0 :
            ANS.append([ind+1, i+1])

    if fugou == 1 :
        if ind+1 != 1 :
            ANS.append([ind+1, 1])
        for i in range(n-1) :
            ANS.append([i+1, i+2])
    else :
        if ind+1 != n :
            ANS.append([ind+1, n])
        for i in range(n,1,-1) :
            ANS.append([i, i-1])

    print(len(ANS))
    for i in range(len(ANS)) :
        print("{} {}".format(ANS[i][0], ANS[i][1]))
else :
    print(0)
