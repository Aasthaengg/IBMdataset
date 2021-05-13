S = input(str())
N = len(S)
X=[[i-1 if S[i]=='L' else i+1 for i in range(N)] if j==0 else [0]*N for j in range(20)]
#print(X)

for k in range(1, 20):
    for i in range(N):
        X[k][i] = X[k-1][X[k-1][i]]
#print(X)

A = [0]*N
for i in range(N):
    A[X[-1][i]] += 1
print(*A)