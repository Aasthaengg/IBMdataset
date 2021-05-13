N, K, Q = map(int, input().split())
A = [0] * Q
Nvec = [0] * N
for i in range(Q):
    A[i] = int(input()) - 1
    Nvec[A[i]] += 1
for n in range(N):
    if (K-Q+Nvec[n])>0:
        print("Yes")
    else:
        print("No")
