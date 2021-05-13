D = int(input())
C = [int(T) for T in input().split()]
S = [[] for TD in range(0,D)]
for TD in range(0,D):
    S[TD] = [int(T) for T in input().split()]
Type = 26
Last = [0]*Type
SatS = 0
Test = [0]*D
for TD in range(0,D):
    SatC = [0]*Type
    for Select in range(0,Type):
        SatC[Select] = S[TD][Select]
        for TC in range(0,Type):
            SatC[Select] -= [C[TC]*(TD+1-Last[TC]),0][TC==Select]
    TesM = SatC.index(max(SatC))
    Last[TesM] = TD+1
    Test[TD] = TesM+1
    SatS += max(SatC)
print('\n'.join(str(TD) for TD in Test))