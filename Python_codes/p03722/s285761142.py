import sys
input = sys.stdin.readline
N, M = [int(x) for x in input().strip().split()]
score = [-float('inf')] * N
score[0] = 0
passed = [False] * N
edges = [0] * M
for m in range(M):
    edges[m] = tuple([int(x) for x in input().strip().split()])

for n in range(N):
    updated = False
    for (i, j, c) in edges:
        # print('i={}, j={}'.format(i, j), end='')
        if score[j-1] < score[i-1] + c:
            score[j-1] = score[i-1] + c
            if j == N-1:
                updated = True
        # print(score)
    if not updated:
        break

if updated:
    print('inf')
else:
    print(score[N-1])