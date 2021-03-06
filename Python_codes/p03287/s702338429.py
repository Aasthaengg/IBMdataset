N,M = map(int,input().split())
A = list(map(int,input().split()))

B = [0 for i in range(N+1)]

for i in range(N):
    B[i+1] += B[i] + A[i]
    B[i+1] %= M

from collections import Counter

counterB = Counter(B)

ans = 0
for v in counterB.values():
    ans += v*(v-1)//2

print(ans)
