N, C, K = map(int, input().split())
T = [int(input()) for _ in range(N)]
T = sorted(T)

S = []
for i in range(N):
    S.append(T[i] + K)
ans = 0
bus = 0
count = 0
for i in range(N):
    if T[i] <= bus and count < C:
        count += 1
    else:
        bus = S[i]
        count = 1
        ans += 1
print(ans)
