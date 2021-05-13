from collections import Counter
N, M = map(int, input().split())
countab = Counter()
for i in range(M):
    a, b = map(int, input().split())
    countab[a] += 1
    countab[b] += 1
ans = True
for k, v in countab.items():
    if v % 2 == 0:
        continue
    ans = False
    break
if ans:
    print('YES')
else:
    print('NO')