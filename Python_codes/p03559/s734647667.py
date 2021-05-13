N = int(input())

A = sorted(list(map(int, input().split())))+[10**10]
B = sorted(list(map(int, input().split())))+[10**10]
C = sorted(list(map(int, input().split())))

cnt = [0]*(N+1)

ai = 0
for bi in range(N):
    while A[ai] < B[bi]:
        ai += 1
    cnt[bi] = ai

for i in range(1, N):
    cnt[i] += cnt[i-1]

ans = 0

bi = 0
for ci in range(N):
    while B[bi] < C[ci]:
        bi += 1
    ans += cnt[bi-1]

print(ans)