import collections
import itertools

H,W = map(int,input().split())

c = [list(map(int,input().split()))for i in range(10)]

a = [list(map(int,input().split()))for i in range(H)]

a_1D =list(itertools.chain.from_iterable(a))

for k in range(10):
    for i in range(10):
        for j in range(10):
            c[i][j] = min(c[i][j],c[i][k]+c[k][j])

a_cnt = collections.Counter(a_1D)

total = 0
for i,j in a_cnt.items():
    if i == -1:
        pass
    else:
        total += c[i][1]*j

print(total)