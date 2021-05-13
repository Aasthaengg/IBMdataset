import math
N,M = (int(T) for T in input().split())
S = input()
T = input()

NMG = math.gcd(N,M)
Length = N*M//NMG
Flag   = True
SIndex = [Nk*(M//NMG) for Nk in range(0,N)]
SList  = list(S)

Count = 0
for Mk in range(0,M):
    if Mk%(M//NMG)==0:
        if SList[Count*(N//NMG)]!=T[Mk]:
            Flag = False
            break
        else:
            Count += 1
if Flag:
    print(Length)
else:
    print(-1)