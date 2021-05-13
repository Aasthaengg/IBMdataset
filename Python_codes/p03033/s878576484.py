from sys import stdin, setrecursionlimit
input = stdin.buffer.readline
setrecursionlimit(10 ** 7)

from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
from collections import deque, defaultdict
from itertools import combinations, permutations, combinations_with_replacement
from itertools import accumulate
from math import ceil, sqrt, pi

MOD = 10 ** 9 + 7
INF = 10 ** 18

N, Q = map(int, input().split())
STX = [list(map(int, input().split())) for _ in range(N)]
D = [int(input()) for _ in range(Q)]

ST = []
for s, t, x in STX:
    ST.append([s - x, t - x])

start = [[] for _ in range(Q + 1)]
end   = [[] for _ in range(Q + 1)]

for i, (s, t) in enumerate(ST):
    si = bisect_left(D, s)
    ti = bisect_left(D, t)
    start[si].append(STX[i][2])
    end[ti].append(STX[i][2])
#print(start)
#print(end)

end_flag = defaultdict(int)
hp = []

for i in range(Q):
    for ed in end[i]:
        end_flag[ed] += 1
    for st in start[i]:
        heappush(hp, st)
    #print(i, hp)
    while 1:
        if hp:
            tmp = heappop(hp)
            if end_flag[tmp]:
                end_flag[tmp] -= 1
            else:
                print(tmp)
                heappush(hp, tmp)
                break
        else:
            print(-1)
            break