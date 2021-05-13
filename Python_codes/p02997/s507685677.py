# -*- coding: utf-8 -*-
#E - Friendships
import sys 
from itertools import combinations
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N, K = map(int,readline().split())
if K > (N-1)*(N-2)//2:
    print(-1)
else:
    # Nを頂点とするスターグラフを考える
    x = (N-1)*(N-2)//2
    rest = x-K
    ans = [(x,N) for x in range(1,N)] + list(combinations(range(1,N),2))
    ans = ans[:N-1+rest]
    print(len(ans))
    for x,y in ans:
        print(x,y)