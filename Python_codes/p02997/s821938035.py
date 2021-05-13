import sys
import itertools

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

# 最大はスター　0から(N-1)C2まで可能
N, K = lr()
max = (N-1) * (N-2) // 2
if K > max:
    print(-1)
    exit()
minus = max - K
print(N - 1 + minus) # 辺の数
# 1を中心とする
for i in range(2, N+1):
    print(1, i)

leaf_com = []
for x in itertools.combinations(range(2, N+1), 2):
    leaf_com.append(x)

for i in range(minus):
    u, v = leaf_com[i]
    print(u, v)

# 38