#import heapq
from collections import deque

n = int(input())
s = [0] * n

for i in range(n):
    s[i] = int(input())

# a = list(map(lambda x: int(x) * (-1), input().split()))
'''
heapq.heapify(s)  # 優先度付きキューに。自動で最小値順に並ぶ。
while (sum(s) % 10 == 0):
    try:
        heapq.heappop(s)
    except IndexError:
        s = [0]
        break
'''
s = sorted(s)

if (sum(s) % 10 != 0):
    tar = sum(s)
else:
    for i, val in enumerate(s):
        tar = sum(s) - val
        if (tar % 10 != 0):
            break
        else:
            for j in range(i):
                tar -= s[j]
                if (tar % 10 != 0):
                    break

# ---------------
print(tar)
