# https://drken1215.hatenablog.com/entry/2020/03/23/004100

import collections
import math

N = int(input())
a = list(map(int,input().split()))
a_counter = collections.Counter(a)

res = 0

for v in a_counter: # 全通り
    res += a_counter[v]*(a_counter[v]-1)//2

for v in a:
    befor = a_counter[v]*(a_counter[v]-1)//2
    after = (a_counter[v]-1)*(a_counter[v]-2)//2
    print(res-befor+after)

