from collections import Counter

N,M = map(int,input().split())
A = list(map(int,input().split()))

S = [0]

for i in range(N):
    S.append((S[-1]+A[i])%M)

C = Counter(S)

ans = 0

for v in C.values():
    ans += v*(v-1)//2

print(ans)