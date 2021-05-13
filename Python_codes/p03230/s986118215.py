import sys
from itertools import combinations

stdin = sys.stdin
 
ri = lambda: int(rs())
rl = lambda: list(map(int, stdin.readline().split()))
rs = lambda: stdin.readline().rstrip()  # ignore trailing spaces

N = ri()
x = int((2 * N) ** (0.5))
if x * (x+1) == 2 * N:
    print('Yes')
else:
    print('No')
    exit()

k = x + 1 #部分集合の個数 
num = 2 * N // k #部分集合の要素数
answer = [[] for _ in range(k)]
for i, (a, b) in enumerate(combinations(range(k), 2), 1):
    answer[a].append(i)
    answer[b].append(i)

print(k)
for a in answer:
    print(num, *a)
