def GCD(a,b):
    S=[a,b]
    S.sort(reverse=True)
    while S[1]>0:
        S2=[S[1],S[0]%S[1]]
        S=S2
    return S[0]
    
try:
    while True:
        a,b=[int(i) for i in input().split(" ")]
        G=GCD(a,b)
        L=int(a*b/G)
        print("%d %d"%(G,L))
except EOFError:
    pass

