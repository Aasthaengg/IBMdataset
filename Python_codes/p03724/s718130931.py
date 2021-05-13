import sys

stdin = sys.stdin
 
ri = lambda: int(rs())
rl = lambda: list(map(int, stdin.readline().split()))
rs = lambda: stdin.readline().rstrip()  # ignore trailing spaces

N, M = rl()
nodes = [0] * (N+1) #0は使わない
for i in range(M):
    a, b = rl()
    nodes[a] += 1
    nodes[b] += 1

print('YES' if all(x%2==0 for x in nodes) else 'NO')