N = int(input())
A = list(map(int, input().split()))
Q = int(input())
B, C = [], []
for i in range(Q):
    b, c = map(int, input().split())
    B.append(b)
    C.append(c)
data = {}
SUM = 0
for i in range(N):
    SUM += A[i]
    if A[i] in data:
        data[A[i]] += 1
    else:
        data[A[i]] = 1
for i in range(Q):
    if B[i] in data:
        SUM += data[B[i]]*(C[i]-B[i])
        if C[i] in data:
            data[C[i]] += data[B[i]]
        else:
            data[C[i]] = data[B[i]]
        data[B[i]] = 0
    print(SUM)