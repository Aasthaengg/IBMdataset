import sys
from collections import Counter
input = sys.stdin.buffer.readline
N = int(input())
D = list(map(int, input().split()))
D = Counter(D)
M = int(input())
T = list(map(int, input().split()))
T = Counter(T)

# print('D, T', D, T)
for key, value in zip(T.keys(), T.values()):
    if D.get(key, 0) < value:
        print('NO')
        exit()
print('YES')
