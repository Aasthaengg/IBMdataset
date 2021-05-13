N, K, Q = map(int, input().split())
A = [int(input()) for _ in range(Q)]
L = [0] * (N+1)
for a in A:
    L[a] += 1
for l in L[1:]:
    print("Yes" if Q-l < K else "No")
