from itertools import product
def norm(x):
    return abs(x[0])+abs(x[1])+abs(x[2])
N,M = map(int,input().split())
X = {i:list(map(int,input().split())) for i in range(N)}
cmax = 0
for x in product((1,-1),repeat=3):
    Y = {i:[X[i][0]+x[0]*10**10,X[i][1]+x[1]*10**10,X[i][2]+x[2]*10**10] for i in range(N)}
    Z = {i:norm(Y[i]) for i in range(N)}
    Z = sorted(list(Z.items()),key=lambda x:x[1],reverse=True)
    A = [0,0,0]
    for j in range(M):
        ind = Z[j][0]
        A[0] += X[ind][0]
        A[1] += X[ind][1]
        A[2] += X[ind][2]
    cmax = max(cmax,norm(A))
print(cmax)