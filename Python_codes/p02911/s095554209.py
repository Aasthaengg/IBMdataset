N,K,Q = map(int,input().split())
A = []
B = []
for j in range(N):
    B.append(K-Q)
for i in range(Q):
    A.append(int(input()))
    B[A[i]-1] += 1
for j in range(N):
    if B[j] >= 1:
        print('Yes')
    else:
        print('No')