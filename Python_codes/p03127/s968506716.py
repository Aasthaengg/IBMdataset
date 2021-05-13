#! python3
# 118_C 体力の最小値を表示
#体力の最小値は体力の最大公約数

import math

N = int(input())
st_list = list(map(int,input().split()))

ans = st_list[0]

for i in range(N):
    ans = math.gcd(ans,st_list[i])
    
print(ans)