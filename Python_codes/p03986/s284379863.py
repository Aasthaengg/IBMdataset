def Solver(X):
    K=0
    P=0

    for s in X:
        if s=="S":
            P+=1
        elif P>0:
            P-=1
        else:
            K+=1

    return 2*K
#================================================
X=input()
print(Solver(X))