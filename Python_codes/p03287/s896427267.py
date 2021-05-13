from collections import defaultdict
N, M = map(int, input().split())
A = list(map(int, input().split()))
T = defaultdict(int)
total = 0
for i in range(N):
    total += A[i]
    total %= M
    T[total] += 1
ans = T[0]
for v in T.values():
    ans += v*(v-1)//2
print(ans)