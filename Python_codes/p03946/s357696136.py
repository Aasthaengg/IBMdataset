N, T = map(int, input().split())
A = list(map(int, input().split()))
dictA = {}
minA = 10**13
maxD = 0
for ai in A:
    minA = min(minA, ai)
    maxD = max(ai-minA, maxD)
    dictA[ai] = True
ans = 0
for ai in A:
    dictA[ai] = False
    if dictA.get(ai + maxD, False):
        ans += 1
print(ans)
