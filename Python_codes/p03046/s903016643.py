import copy
M, K =map(int,input().split())
if M == 1:
    if K == 0:
        print('0 0 1 1')
    else:
        print(-1)
elif K == 0:
    ANSL = []
    for i in range(2**M):
        ANSL.append(str(i))
        ANSL.append(str(i))
    ANS = ' '.join(ANSL)
    print(ANS)
elif K <= 2**M-1:
    LI = []
    for i in range(2**M):
        LI.append(2**M-1-i)
    LI.pop(2**M-K-1)
    CI = copy.copy(LI)
    CI.sort()
    AN = [K]+LI+[K]+CI
    ANSL =[str(s) for s in AN]
    ANS = ' '.join(ANSL)
    print(ANS)
else:
    print(-1)
