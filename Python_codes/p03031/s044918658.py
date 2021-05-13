from itertools import product
N, M = map(int, input().split())
S = []
for m in range(M):
    s = list(map(int, input().split()))
    S.append(s[1:])
    
p = list(map(int, input().split()))

ans = 0
for c in product([0, 1], repeat = N):
    ok = True
    for m in range(M):
        sm = 0
        for k in S[m]:
            sm += c[k - 1]
        if sm % 2 != p[m]:
            ok = False
            break
    if ok:
        ans += 1
print(ans)

