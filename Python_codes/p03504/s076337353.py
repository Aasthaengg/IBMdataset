# D - Recording

N, C = map(int, input().split())
max_time = 10**5
gantt = [[0] * (max_time + 1) for _ in range(C+1)]
stc = []

for _ in range(N):
    stc.append(list(map(int, input().split())))
    
stc = sorted(stc, key = lambda x: x[0])
stc = sorted(stc, key = lambda x: x[2])    

for idx in range(N):
    s, t, c = stc[idx][0], stc[idx][1], stc[idx][2]
    try:
        if stc[idx-1][2] == c and stc[idx-1][1] == s:
            gantt[c][s+1] += 1
        else:
            gantt[c][s] += 1
    except IndexError:
        gantt[c][s] += 1
    if t+1 <= max_time:
        gantt[c][t+1] -= 1

for c in range(C+1):
    for idx in range(1, max_time+1):
        gantt[c][idx] += gantt[c][idx-1]
    
import numpy as np
print(np.max(np.sum(gantt, axis = 0)))