N=int(input())
hp_list = list(map(int,input().split()))

from functools import reduce
from fractions import gcd

max=0
min=10**9+1
for i in range(N):#O(10**5)
    if max < hp_list[i]:
        max = hp_list[i]
        max_index = i
    if min > hp_list[i]:
        min = hp_list[i]
        min_index = i
    tmp_list=[max,min]
    hp_list[max_index]=reduce(gcd,tmp_list)
#print(max,min)
#print(max_index,min_index)
hp_list = sorted(hp_list, reverse=False)
print(hp_list[0])