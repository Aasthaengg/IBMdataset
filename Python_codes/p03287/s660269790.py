import numpy as np
n,m = map(int,input().split())
l = list(map(int,input().split()))
c = np.cumsum([0]+l).tolist()
lst = [i%m for i in c]
dic = {}
res = 0
for l in lst:
    if l in dic.keys():
        res += dic[l]
        dic[l] = dic[l] + 1
    else:
        dic[l] = 1
print(res)