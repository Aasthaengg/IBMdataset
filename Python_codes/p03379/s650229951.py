N = int(input())
X = [int(T) for T in input().split()]
SortX = sorted(X)
MedL  = SortX[(N//2)-1]
MedR  = SortX[(N//2)]
if MedL==MedR:
    Disp = [str(MedL)]*N
    print('\n'.join(Disp))
else:
    Disp = [0]*N
    for T in range(0,N):
        if X[T] <=MedL:
            Disp[T] = str(MedR)
        else:
            Disp[T] = str(MedL)
    print('\n'.join(Disp))