
from operator import itemgetter
n = int(input())
t = [list(map(int,input().split())) for i in range(n)]

t.sort(key=lambda x: x[1])
cost = 0
for i in t:
    cost += i[0]
    if cost > i[1]:
        print('No')
        exit()
print('Yes')