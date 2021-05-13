from collections import Counter

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

S = [0]

for a in A:
    S.append((S[-1]+a)%M)

c = Counter()
ans = 0

for s in S:
    ans += c[s]
    c[s] += 1
    
print(ans)