from bisect import bisect

N =int(input())
A = sorted(list(map(int,input().split())))

ans = []

if len(A) == 2 :
    ans.append(A[::-1])
    calc = A[1] - A[0]

else :
    ind = bisect(A,0)

    X = A[:ind]
    Y = A[ind:]
    
    if len(X) == 0 :
        ans.append([Y[0],Y[1]])
        X.append(Y[0]-Y[1])
        Y.pop(0)
        Y.pop(0)
    elif len(Y) == 0 :
        ans.append([X[-1],X[-2]])
        Y.append(X[-1]-X[-2])
        X.pop(-1)
        X.pop(-1)
    
    while True :
        if len(X) >= 2 :
            ans.append([Y[0],X[-1]])
            Y[0] -= X.pop(-1)
        elif len(Y) >= 2 :
            ans.append([X[-1],Y[0]])
            X[-1] -= Y.pop(0)
        else :
            ans.append([Y[0],X[0]])
            calc = Y.pop(0) - X.pop(0)
            break
    
print(calc)
for i in range(len(ans)) :
    print(*ans[i])
