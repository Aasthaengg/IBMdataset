n = int(input())
l = list(map(int, input().split()))

from collections import Counter
c = Counter(l)
c = sorted(c.items(), reverse=1)

temp = 0
for i in range(len(c)):
    if c[i][1] >= 2:
        if temp != 0:
            print(temp * c[i][0])
            exit()
        else:
            temp = c[i][0]
    if c[i][1] >= 4:
            print(c[i][0] ** 2)
            exit()
else:
    print(0)