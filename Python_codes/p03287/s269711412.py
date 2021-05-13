from collections import Counter
N, M = map(int, input().split())
S = [0]
for a in map(int, input().split()):
    S.append((a + S[-1])%M)
res = 0
for v in Counter(S).values():
    res += v*(v-1)//2
print(res)