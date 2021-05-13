from collections import Counter
N, M = map(int, input().split())
A = list(map(lambda x:int(x)%M, input().split()))
B = A[:]
for i in range(N-1):
    B[i+1] += B[i]
    B[i+1] %= M
c = Counter(B)


ans = 0
for k, v in c.items():
    if k == 0:
        ans += v
    if v >= 2:
        ans += v*(v-1)//2
print(ans)