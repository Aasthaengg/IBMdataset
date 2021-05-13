x, y = map(int, input().split())
from collections import defaultdict
dic = defaultdict(lambda: 0)
dic[1] = 300000
dic[2] = 200000
dic[3] = 100000
if x == 1 and y == 1:
    print(1000000)
else:
    print(dic[x]+dic[y])