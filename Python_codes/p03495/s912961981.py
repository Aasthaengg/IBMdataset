n, k = map(int, input().split())

from collections import Counter
c = Counter(list(map(int, input().split())))

#Counterからの取り出し
l = []
m = []
for x, y in c.items():
    l += [y]
    m += [x]

L = sorted(l)
M = len(m)

cnt = 0 
if M <= k:
    print(0)
else:
    for i in range(M-k):
        cnt += L[i]
    print(cnt)