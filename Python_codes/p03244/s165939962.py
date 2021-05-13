import collections
N = int(input())
V = [int(X) for X in input().split()]

if len(set(V))==1:
    print(N//2)
else:
    OddV  = V[::2]
    EvenV = V[1::2]
    LenOddV  = len(set(OddV))
    LenEvenV = len(set(EvenV))
    if LenOddV==1 and LenEvenV==1:
        NOddV  = OddV[0]
        NEvenV = EvenV[0]
        print(0)
    elif LenOddV!=1 and LenEvenV==1:
        OddCount = collections.Counter(OddV)
        NEvenV   = EvenV[0]
        if OddCount.most_common()[0][0]==NEvenV:
            NOddV = OddCount.most_common()[1][0]
            print(N//2-OddCount.most_common()[1][1])
        else:
            NOddV = OddCount.most_common()[0][0]
            print(N//2-OddCount.most_common()[0][1])
    elif LenOddV==1 and LenEvenV!=1:
        NOddV     = OddV[0]
        EvenCount = collections.Counter(EvenV)
        if EvenCount.most_common()[0][0]==NOddV:
            NEvenV = EvenCount.most_common()[1][0]
            print(N//2-EvenCount.most_common()[1][1])
        else:
            NEvenV = EvenCount.most_common()[0][0]
            print(N//2-EvenCount.most_common()[0][1])
    elif LenOddV!=1 and LenEvenV!=1:
        OddCount  = collections.Counter(OddV)
        EvenCount = collections.Counter(EvenV)
        if OddCount.most_common()[0][0]!=EvenCount.most_common()[0][0]:
            NOddV  = OddCount.most_common()[0][0]
            NEvenV = EvenCount.most_common()[0][0]
            print(N-OddCount.most_common()[0][1]-EvenCount.most_common()[0][1])
        else:
            if OddCount.most_common()[0][1]>EvenCount.most_common()[0][1]:
                NOddV  = OddCount.most_common()[0][0]
                NEvenV = EvenCount.most_common()[1][0]
                print(N-OddCount.most_common()[0][1]-EvenCount.most_common()[1][1])
            elif OddCount.most_common()[0][1]<EvenCount.most_common()[0][1]:
                NOddV  = OddCount.most_common()[1][0]
                NEvenV = EvenCount.most_common()[0][0]
                print(N-OddCount.most_common()[1][1]-EvenCount.most_common()[0][1])
            else:
                if OddCount.most_common()[1][1]>=EvenCount.most_common()[1][1]:
                    NOddV  = OddCount.most_common()[1][0]
                    NEvenV = EvenCount.most_common()[0][0]
                    print(N-OddCount.most_common()[1][1]-EvenCount.most_common()[0][1])
                elif OddCount.most_common()[1][1]<EvenCount.most_common()[1][1]:
                    NOddV  = OddCount.most_common()[0][0]
                    NEvenV = EvenCount.most_common()[1][0]
                    print(N-OddCount.most_common()[0][1]-EvenCount.most_common()[1][1])