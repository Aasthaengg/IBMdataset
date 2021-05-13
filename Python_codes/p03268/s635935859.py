n,k = map(int,input().split())
# 1 ~ n で、kで割った余りがどれだけあるか
from collections import defaultdict
dic = defaultdict(int)
for i in range(1,n+1): # 0含んだらダメじゃん
    dic[i%k] += 1
res = 0
for a in range(k):
    # 余りで考える
    b = (k-a)%k
    c = (k-a)%k
    if ((b+c)%k != 0):
        continue
    res += dic[a]*dic[b]*dic[c]
print(res)
