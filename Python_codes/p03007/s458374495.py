N = int(input())
A = list(map(int,input().split()))
A = sorted(A,reverse=True)
Y, X = [A[0]], [A[-1]]
for i in range(1, N-1):
    if A[i] >= 0:
        Y.append(A[i])
    else:
        X.append(A[i])
res = []

for i in range(len(Y)-1,0,-1) :
    res.append([X[-1],Y[i]])
    X[-1] -= Y[i]

for i in range(len(X)-1,-1,-1) :
    res.append([Y[0],X[i]])
    Y[0] -= X[i]

print(Y[0])
for r in res :
    print(*r)
