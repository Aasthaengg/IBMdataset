N = int(input())
S = [input() for _ in range(N)]

ab = 0
lastA = 0
onlylastA = 0
firstB = 0
onlyfirstB = 0
for s in S:
    ab += s.count('AB')
    if s[-1] == 'A' and s[0] != 'B':
        lastA += 1
        onlylastA += 1
    if s[0] == 'B' and s[-1] != 'A':
        firstB += 1
        onlyfirstB += 1
    if s[-1] == 'A' and s[0] == 'B':
        lastA += 1
        firstB += 1

ans = ab + min(lastA,firstB)
if lastA != 0 and onlylastA == 0 and onlyfirstB == 0:
    ans = max(ans-1,0)
print(ans)