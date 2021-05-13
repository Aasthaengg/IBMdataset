from collections import deque
N,M,P = map(int, input().split())
R = []
R2 = {}
R3 = {}
OPT = [float("inf")]*(N+1)
for _ in range(M):
    A,B,C = map(int, input().split())
    R.append([A,B,-C+P])
    if not B in R2:
        R2[B] = []
    if not A in R3:
        R3[A] = []
    R3[A].append(B)
    R2[B].append(A)

visited_N = [0]*(N+1)
visited_N[N] = 1
queue = deque()
queue.append(N)

while queue != deque():
    tmp = queue.pop()
    if tmp in R2:
        for i in R2[tmp]:
            if visited_N[i] == 0:
                visited_N[i] = 1
                queue.append(i)    

visited_1 = [0]*(N+1)
visited_1[1] = 1
queue = deque()
queue.append(1)

while queue != deque():
    tmp = queue.pop()
    if tmp in R3:
        for i in R3[tmp]:
            if visited_1[i] == 0:
                visited_1[i] = 1
                queue.append(i)    

visited = [0]*(N+1)
for i in range(N):
    visited[i+1] = visited_N[i+1]*visited_1[i+1]
                
OPT[1] = 0
OPT_tmp = OPT

for _ in range(N-1):
    for i in range(M):
        tmp_r = R[i]
        if visited[tmp_r[0]] == 1 and visited[tmp_r[1]] == 1:
            if OPT[tmp_r[0]] + tmp_r[2] < OPT[tmp_r[1]]:
                OPT[tmp_r[1]] = OPT[tmp_r[0]] + tmp_r[2]
    OPT = OPT_tmp
tmp_opt = OPT[N]

flag = 0
for i in range(M):
    tmp_r = R[i]
    if visited[tmp_r[0]] == 1 and visited[tmp_r[1]] == 1:
        if OPT[tmp_r[0]] + tmp_r[2] < OPT[tmp_r[1]]:
            flag = 1
    
if flag:
    answer = -1
else:
    answer = max(0,-tmp_opt)

print(answer)