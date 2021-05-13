#!/usr/bin/env python3
#エイシングプログラミングコンテスト2019 C

import sys
import math
import bisect
sys.setrecursionlimit(1000000000)
from heapq import heappush, heappop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
mod = 10**9 + 7
inf = float('inf')
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))


dx,dy = [1,0,-1,0],[0,1,0,-1]
h,w = LI()
s = [input() for _ in range(h)]
que = deque()
ch = [[-1]*w for _ in range(h)]
ans = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            if ch[i][j] < 0:
                ch[i][j] = 0
                que = deque()
                que.append((i,j))
                #a:= ルールを守りながら行ける#の数
                #b:= ルールを守りながら行ける.の数
                a,b = 1,0
                while que:
                    y,x = que.popleft()
                    for k in range(4):
                        nx,ny = x + dx[k], y + dy[k]
                        if 0 <= nx < w and 0 <= ny < h and ch[ny][nx] < 0:
                            if s[y][x] != s[ny][nx]:
                                if s[ny][nx] == '#':
                                    a += 1
                                else:
                                    b += 1
                                ch[ny][nx] = 0
                                que.append((ny,nx))
                ans += a*b
print(ans)
