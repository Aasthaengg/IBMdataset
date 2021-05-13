N, K, Q = map(int, input().split())
A = [int(input()) for i in range(Q)]
a = [0] * N
for i in range(Q):
    a[A[i]-1] += 1
for i in range(N):
    if K - ( Q - a[i] ) > 0:
        print('Yes')
    else:
        print('No')
