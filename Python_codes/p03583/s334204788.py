import sys
from collections import Counter

stdin = sys.stdin
 
ri = lambda: int(rs())
rl = lambda: list(map(int, stdin.readline().split()))
rs = lambda: stdin.readline().rstrip()  # ignore trailing spaces
sys.setrecursionlimit(10 ** 8)

N = ri()
#一番小さい数をhとして良い
for i in range(N//4, 3501):
    for j in range(i, 3501):
        if 4*i*j-N*i-N*j == 0:
            continue
        w = (N*i*j)/(4*i*j-N*i-N*j)
        if w > 0 and w.is_integer():
            print(i, j, int(w))
            exit()