#B - Contest with Drinks Easy
N = int(input())
T = list(map(int,input().split()))
M = int(input())
P = []
X = []
for _ in range(M):
    Pi,Xi = map(int,input().split())
    P.append(Pi)
    X.append(Xi)

A = []
for i in range(M):
    T_copy = T.copy()
    T_copy[P[i]-1] = X[i]
    A.append(sum(T_copy))    

for k in range(M):
    print(A[k])