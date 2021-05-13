n = int(input())
S = input()
from collections import Counter
dic = Counter(S)
#print(dic)
mod = 10**9 + 7
res = 1
for k,v in dic.items():
    res *= v + 1
    res %= mod
# 最後に
print((res + mod - 1)%mod)
