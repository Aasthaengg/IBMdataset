N, M = map(int, input().split())
H = list(map(int, input().split()))
ma = [0 for i in range(N)]
A, B = [], []
ans = 0

for i in range(M):
    a, b = map(int, input().split())
    ma[a-1] = max(ma[a-1], H[b-1])
    ma[b-1] = max(ma[b-1], H[a-1])

for j in range(N):
    if H[j] > ma[j]:
        ans += 1

print(ans)
