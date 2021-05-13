import sys
 
N = int(input())
 
A =[ [0 for i in range(2)]for i in range(20)]
 
if N < 20:
    for i in range(N):

        print(i)
        print("", flush=True)
    
    S = input()
    if S == 'Vacant':
        sys.exit()
 
else:
    nS = 0
    nE = N - 1
    
    nQ = 0 
    print(nQ)
    print("", flush=True) 
    S = input()
    if S == 'Vacant':
        sys.exit()
 
 
    nQ = N - 1
    print(nQ)
    print("", flush=True)
    E = input()
    if E == 'Vacant':
        sys.exit()
 
    for i in range(20):
        nQ = ( nS + nE ) // 2
        print(nQ)
        print("", flush=True)
    
        S1 = input()
        if S1 == 'Vacant':
            sys.exit()
 
        nT2 = (nQ - nS) % 2
 
        if ( nT2 != 0 ) and ( S ==S1 ):
            E = S1
            nE = nQ
        elif ( nT2 == 0 ) and ( S !=S1 ):
            E = S1
            nE = nQ
        elif ( nT2 != 0 ) and ( S !=S1 ):
            S = S1
            nS = nQ
        elif ( nT2 == 0 ) and ( S ==S1 ):
            S = S1
            nS = nQ
