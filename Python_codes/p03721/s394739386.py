N,K = (int(T) for T in input().split())
Ins = [[] for T in range(0,N)]
for TN in range(0,N):
    Ins[TN] = [int(T) for T in input().split()]
InsSort = sorted(Ins)
Total = 0
for TN in range(0,N):
    if Total<K<=Total+InsSort[TN][1]:
        print(InsSort[TN][0])
        break
    else:
        Total += InsSort[TN][1]