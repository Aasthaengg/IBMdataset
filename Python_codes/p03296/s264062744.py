N = int(input())
A = list(map(int, input().split()))

chunk = []
now = 1
for i in range(1, N):
    if A[i] == A[i - 1]:
        now += 1
    else:
        if now != 1:
            chunk.append(now)
            now = 1
    if i == N - 1 and now != 1:
        chunk.append(now)
ans = 0
for c in chunk:
    ans += c // 2

print(ans)

