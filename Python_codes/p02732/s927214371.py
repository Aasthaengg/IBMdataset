n = int(input())
l = list(map(int, input().split()))

from collections import Counter
c = Counter(l)

num = [[] for _ in range(n+1)]

tot = 0
for i,j in c.items():
    if j >= 2:
        tmp1 = j*(j-1)//2
        tot += tmp1
    else:
        tmp1 = 0
    if j >= 3:
        tmp2 = (j-1)*(j-2)//2
    else:
        tmp2 = 0
    num[i] = [tmp1, tmp2]

for k in l:
    print(tot - num[k][0] + num[k][1])
