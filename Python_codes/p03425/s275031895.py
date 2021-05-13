from collections import Counter
import itertools

n = int(input())

s = [str(input()) for _ in range(n)]
initial = []
d = ['M', 'A', 'R', 'C', 'H']

for i in range(n):
    if s[i][0] in d:
        initial.append(s[i][0])

reg = Counter(initial)
ele = []

for i, j in reg.items():
    ele.append(i)
ans = 0
for A in itertools.combinations(ele, 3):
    #print(A)
    cnt = 1
    for s in A:
        cnt *= reg[s]
    ans += cnt

print(ans)