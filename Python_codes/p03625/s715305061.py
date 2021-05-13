from collections import Counter
n = int(input())
A = list(map(int, input().split()))

C = Counter(A)

rec = []
squ = []

for a in A:
    if 2 <= C[a]:
        rec.append(a)
    if 4 <= C[a]:
        squ.append(a)
rec = list(set(rec))
squ = list(set(squ))
# print(rec)
# print(squ)

s = 0
if len(squ) != 0:
    s = max(squ)**2

if len(rec) < 2:
    print(s)
else:
    rec.sort(reverse=True)
    print(max(s, rec[0]*rec[1]))