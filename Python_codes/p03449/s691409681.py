N = int(input())
A1 = [int(X) for X in input().split()]
A2 = [int(X) for X in input().split()]
CumSumA1 = [A1[0]]*N
CumSumA2 = [A2[(N-1)]]*N
Disp = [0]*N
for T in range(0,N-1):
    CumSumA1[T+1] = CumSumA1[T]+A1[T+1]
    CumSumA2[(N-1)-(T+1)] = CumSumA2[(N-1)-T]+A2[(N-1)-(T+1)]
for T in range(0,N):
    Disp[T] = CumSumA1[T]+CumSumA2[T]
print(max(Disp))