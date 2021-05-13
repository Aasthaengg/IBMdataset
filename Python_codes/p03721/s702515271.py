N, K = map(int,input().split())
A = []
B = []

for i in range(N):
    a = list(map(int, input().split()))
    A.append(a)

A = sorted(A)

ss = [0]*(N+1)
ss[0] = A[0][1]

for i in range(1, N):
    ss[i] = ss[i-1] + A[i][1]
    if ss[i-1] < K <= ss[i]:
        print(A[i][0])
        exit()
    else:
        pass
