N = int(input())
TT = [int(i) for i in input().split()]
M = int(input())
PP = []
XX = []
for _ in range(M):
    P, X = [int(i) for i in input().split()]
    PP.append(P)
    XX.append(X)

maxTime = 0
sumTime = sum(TT)
for i in range(len(PP)):
    print(sumTime - (TT[PP[i] - 1] - XX[i]))
