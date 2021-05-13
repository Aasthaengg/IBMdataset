N, T = map(int, input().split())
A = [int(i) for i in input().split()]

Amin = 10**10
P = -10**10
c = 0
for i in range(N):
    if A[i] < Amin:
        Amin = A[i]

    if A[i]-Amin == P:
        c += 1
    elif A[i]-Amin > P:
        P = A[i]-Amin
        c = 1
print(c)
