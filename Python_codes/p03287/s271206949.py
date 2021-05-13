from collections import Counter

N, M = map(int, input().split())
A = list(map(int, input().split()))
cum = [0]*(N+1)
cum[0] = 0
for i in range(1, N+1):
    cum[i] = cum[i-1] + A[i-1]

cum = [cum[i]%M for i in range(N+1)]
cnt = Counter(cum)
ans = 0
for k, v in cnt.items():
    ans += v*(v-1)//2
print(ans)