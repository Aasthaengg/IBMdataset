# C - AtCoDeerくんと選挙速報 / AtCoDeer and Election Report

# 比がa:bとなる合計最小の票分布はa,b
# 次にc:dになったとき、a<=cかつb<=dとなるようにc,dに同じ数をかける

import math

N = int(input())
TA = [list(map(int, input().split())) for _ in range(N)]

a, b = TA[0]
c, d = a, b

for idx in range(1,N):
    c, d = TA[idx]
    multi = max((a+c-1)//c, (b+d-1)//d)
    c *= multi
    d *= multi
    a,b = c,d
    
print(c+d)