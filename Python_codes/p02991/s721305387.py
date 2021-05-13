from collections import deque
import sys
input = sys.stdin.readline
'''
allinputs = iter(input().splitlines())
input = lambda : next(allinputs)
#'''
N, M = map(int, input().split())
edge = [[] for _ in range(N)]

for _ in range(M):
	u, v = map(int, input().split())
	u -= 1
	v -= 1
	edge[u].append(v)
	
S, T = map(int, input().split())
S -= 1
T -= 1
has_reached = [[-1] * N for _ in range(3)]
q = [deque() for _ in range(3)]
q[0].append(S)
has_reached[0][S] = 0
i = 0

while q[0] or q[1] or q[2]:
	if q[i]:
		now_node = q[i].popleft()
		for next_node in edge[now_node]:
			if has_reached[i - 2][next_node] < 0:
				has_reached[i - 2][next_node] = has_reached[i][now_node] + int(i == 0)
				q[i - 2].append(next_node)
			
	i = (i + 1) % 3
	
print(has_reached[0][T])
'''
for i in range(3):
	print(has_reached[i])
'''