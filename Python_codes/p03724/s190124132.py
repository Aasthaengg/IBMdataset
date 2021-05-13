import sys
input = sys.stdin.readline
from collections import *

N, M = map(int, input().split())
dic = defaultdict(int)
for i in range(M):
    a, b = map(int, input().split())
    dic[a] += 1
    dic[b] += 1
if any([x&1 for x in dic.values()]):
    print('NO')
else:
    print('YES')