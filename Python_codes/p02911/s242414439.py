from collections import Counter
n ,k, q = map(int,input().split())
al = []
for _ in range(q):
    al.append(int(input()))

if k > q:
    for _ in  range(n):
        print('Yes')
    exit()

Ca = Counter(al)

for i in range(1,n+1) :
    if Ca[i] >= q-k + 1:
        print('Yes')
    else:
        print('No')