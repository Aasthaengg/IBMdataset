N, K, Q = map(int, input().split())
A = []
point = [0] * N
for i in range(Q):
    A.append(int(input()))
    point[A[i]-1] += 1

for i in range(N):
    if K - Q + point[i] >= 1:
        print('Yes')
    else:
        print('No')