K, N = map(int, input().split())
A = list(map(int, input().split()))

dis = [0] * N
for i in range(N):
    if i == N-1:
        dis[i] = K - A[i] + A[0]
    else:
        dis[i] = A[i+1] - A[i]

print(K-max(dis))