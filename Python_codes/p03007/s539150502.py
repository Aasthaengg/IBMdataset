import bisect

N = int(input())
A = list(map(int,input().split()))

ans = []

A = sorted(A)

if N == 2 :
    ans.append([A[1],A[0]])
    calc = A[1] - A[0]

else :
    ind = bisect.bisect_left(A,0)

    X = A[:ind]
    Y = A[ind:]
    
    if len(X) == 0 :
        ans.append([Y[0],Y[1]])
        X.append(Y.pop(0)-Y.pop(0))
    
    elif len(Y) == 0 :
        ans.append([X[-1],X[-2]])
        Y.append(X.pop(-1)-X.pop(-1))
    
    while len(Y) != 1 :
        ans.append([X[-1],Y[0]])
        X[-1] -= Y.pop(0)
    
    while len(X) :
        ans.append([Y[0],X[-1]])
        Y[0] -= X.pop(-1)
    
    calc = Y.pop(0)

print(calc)
for a in ans :
    print(*a)
