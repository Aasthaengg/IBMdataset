N, K, Q = map(int, input().split())
ans = [0] * N
for _ in range(Q):
    A = int(input())
    ans[A-1] += 1
for i in range(N):
     print('Yes' if K - Q + ans[i] > 0 else 'No')
