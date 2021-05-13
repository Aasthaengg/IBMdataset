from math import ceil
N,K =map(int,input().split())
A = list(map(int,input().split()))
X1 = 1
X2 = 10**9
while X1 != X2-1:
    X = ceil((X1 + X2)/2)
    S = 0
    for i in range(N):
        S += ceil(A[i]/X) - 1
    if S <= K:
        X2 = X
    else:
        X1 = X
S1 = 0
for i in range(N):
    S += ceil(A[i]/X2) - 1
if S <= K:
    X2 = X1
print(X2)