import sys
from bisect import *
input = sys.stdin.buffer.readline

INF = 10 ** 13

A, B, Q = map(int, input().split())
shrines = [-INF] + [int(input()) for _ in range(A)] + [INF]
temples = [-INF] + [int(input()) for _ in range(B)] + [INF]
queries = [int(input()) for _ in range(Q)]

for x in queries:
    s_index = bisect(shrines, x)
    t_index = bisect(temples, x)
    rs = shrines[s_index]
    rt = temples[t_index]
    ls = shrines[s_index - 1]
    lt = temples[t_index - 1]
    ans = INF
    ans = min(ans, max(rs, rt) - x)
    ans = min(ans, x - min(ls, lt))
    ans = min(ans, (rt - ls)*2 - max(rt-x, x-ls))    
    ans = min(ans, (rs - lt)*2 - max(rs-x, x-lt))
    print(ans)
    
     
