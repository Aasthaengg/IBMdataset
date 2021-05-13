from itertools import accumulate
from collections import Counter
N = int(input())
S = list(input())
kuro = [0]*N
shiro = [0]*N
ans = N

for i in range(N):
    if S[i] == "#":
        kuro[i] = 1
    else:
        shiro[i] = 1
shiro.reverse()
shiro = list(accumulate(shiro))
kuro = list(accumulate(kuro))

for i in range(N-1):
    ans = min(ans, kuro[i]+shiro[N-i-2])

ans = min(ans, kuro[N-1])
S = Counter(S)
ans = min(ans, S["#"], S["."])
print(ans)
