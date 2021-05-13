from collections import defaultdict
N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))
ad = defaultdict(lambda: -1)
i, j = 0, 0
while i < N and j < N:
    if A[i] < B[j]:
        ad[i] = j
        i += 1
    else:
        j += 1
bd = defaultdict(lambda: -1)
i, j = 0, 0
while i < N and j < N:
    if B[i] < C[j]:
        bd[i] = j
        i += 1
    else:
        j += 1
csum = [0] * N
for i in range(N):
    if bd[i] >= 0:
        csum[i] = N-bd[i]
bsum = [0]* N
cnt = 0
for i in range(N):
    cnt += csum[N-1-i]
    bsum[N-1-i] = cnt
ans = 0
for i in range(N):
    if ad[i] >= 0:
        ans += bsum[ad[i]]
print(ans)