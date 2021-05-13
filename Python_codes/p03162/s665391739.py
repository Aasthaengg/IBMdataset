from functools import lru_cache

n = int(input())
action = []
for i in range(n):
    action.append(list(map(int,input().split())))

@lru_cache(maxsize=None)
def dp(i, a):
    if i == 0:
        return action[0][a]
    else:
        return max(dp(i-1, (a+1)%3), dp(i-1, (a+2)%3)) + action[i][a]

import sys
sys.setrecursionlimit(1000000)
print(max([dp(n-1,a) for a in range(3)]))
