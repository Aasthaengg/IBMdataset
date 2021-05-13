n, m, q = map(int,input().split())
query = []
for i in range(q):
    query.append(list(map(int, input().split())))

#print(query)

import itertools
cnbr = []  #組み合わせ
for i in range(m+1):
    for j in itertools.combinations_with_replacement(range(m), n):
        cnbr.append(j)

#print(cnbr)
points = [0] * len(cnbr)

for _ in range(len(cnbr)):
    for a,b,c,d in query:
        if cnbr[_][b - 1] - cnbr[_][a - 1] == c:
            points[_] += d

print(max(points))