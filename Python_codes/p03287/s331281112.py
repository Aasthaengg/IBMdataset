
import math
from itertools import accumulate

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


n,m = map(int,input().split())

A = list(map(int,input().split()))


accum_A = [0] + A
accum_A = list(accumulate(accum_A))

mod_dic = {}

for i in accum_A:
    mod = i%m
    
    if mod in mod_dic.keys():
        mod_dic[mod] += 1
    else:
        mod_dic[mod] = 1

ans = 0
    
for i in mod_dic.values():
    if i >= 2:
        ans += combinations_count(i,2)
    
print(ans)

