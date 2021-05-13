import math
N,M = (int(T) for T in input().split())
S = input()
T = input()

NMgcd = math.gcd(N,M)
Leng  = N*M//NMgcd
Flag  = True
SList = [S[Nk] for Nk in range(0,N) if Nk%(N//NMgcd)==0]

for Mk in range(0,len(SList)):
    if SList[Mk]!=T[Mk*(M//NMgcd)]:
        Flag = False
        break
if Flag:
    print(Leng)
else:
    print(-1)