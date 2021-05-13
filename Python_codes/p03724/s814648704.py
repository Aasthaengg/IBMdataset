N, M = map(int, input().split())
X = [0] * N
for _ in range(M):
    a, b = map(int, input().split())
    X[a-1] ^= 1
    X[b-1] ^= 1

print("YES" if sum(X) == 0 else "NO")