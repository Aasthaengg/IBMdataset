from collections import deque
import sys
#input = sys.stdin.readline

N = int(input().strip("\n"))
A = [list(map(lambda x :int(x)-1, input().split())) for _ in range(N)]

# 対戦カード (インデックス0>インデックス[1]だけ使う)
all_patterns = [[[] for _ in range(N)] for _ in range(N)]
lines_to_here = [[0 for _ in range(N)] for _ in range(N)]

for i in range(len(A)):
    for j in range(len(A[i])-1):
        playerA = i
        playerB = A[i][j]
        if playerA < playerB:
            playerA, playerB = playerB, playerA
        next_playerA = i
        next_playerB = A[i][j+1]
        if next_playerA < next_playerB:
            next_playerA, next_playerB = next_playerB, next_playerA
        
        all_patterns[playerA][playerB].append((next_playerA,next_playerB))
        lines_to_here[next_playerA][next_playerB] += 1

next_out = deque()
for i in range(1,N):
    for j in range(i):
        if lines_to_here[i][j] == 0:
            next_out.append([i,j])

if len(next_out) == 0:
    print(-1)
    sys.exit()
    

indexin_topological_sorted = [[0 for _ in range(N)] for _ in range(N)]

# topological sort
topological_sorted = []
while len(next_out) > 0:
    added = next_out.pop()
    topological_sorted.append(added)
    indexin_topological_sorted[added[0]][added[1]] = len(topological_sorted)-1
    for direction in all_patterns[added[0]][added[1]]:
        lines_to_here[direction[0]][direction[1]]-=1
        if lines_to_here[direction[0]][direction[1]] == 0:
            next_out.append(direction)

# if there is closed circuit, number remain(not 0 exists)
for i in range(1,N):
    for j in range(i):
        if lines_to_here[i][j] > 0:
            print(-1)
            sys.exit()

costs = [0 for _ in range(len(topological_sorted))]

max_cost = 0
for i in range(len(topological_sorted)):
    processing = topological_sorted[i]
    now_cost = costs[i]
    for direction in all_patterns[processing[0]][processing[1]]:
        direction_in_topological_sorted = indexin_topological_sorted[direction[0]][direction[1]]        
        costs[direction_in_topological_sorted] = max(1+now_cost,costs[direction_in_topological_sorted])
        max_cost = max(max_cost,costs[direction_in_topological_sorted])
print(max_cost+1)
