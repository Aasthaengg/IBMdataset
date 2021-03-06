def FindParent(X):
    if Parent[X]==X:
        return X
    else:
        Parent[X] = FindParent(Parent[X])
        return Parent[X]

def CheckParent(X,Y):
    return FindParent(X)==FindParent(Y)

def UniteParent(X,Y):
    X = FindParent(X)
    Y = FindParent(Y)
    if X==Y:
        return 0
    if Rank[X]<Rank[Y]:
        Parent[X] = Y
    else:
        Parent[Y] = X
        if Rank[X]==Rank[Y]:
            Rank[X] += 1

import copy
N,M = (int(T) for T in input().split())
List = [[] for TM in range(0,M)]
for TM in range(0,M):
    List[TM] = [int(T) for T in input().split()]
    
Count = 0
for TM in range(0,M):
    ListCopy = copy.deepcopy(List)
    del ListCopy[TM]
    
    Parent = [I for I in range(N+1)]
    Rank = [0]*(N+1)
    for TTM in range(0,M-1):
        UniteParent(ListCopy[TTM][0],ListCopy[TTM][1])

    if not CheckParent(List[TM][0],List[TM][1]):
        Count += 1
print(Count)