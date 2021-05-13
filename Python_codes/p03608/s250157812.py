import copy
from collections import deque
n, m, r = map(int,input().split())
R = list(map(int, input().split()))

f_inf = float('inf')
wf = [[f_inf for _ in range(n+1)] for __ in range(n+1)]

tree = [[] for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    wf[a][b] = c
    wf[b][a] = c
for i in range(1, n+1):
    wf[i][i] = 0
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            wf[i][j] = min(wf[i][j], wf[i][k]+wf[k][j])

all_type = []
def get_all_type(r, info, lon):
    if lon == len(info):
        return [info]
    result = []
    for i in r:
        if i in info:
            continue
        else:
            next_info = copy.deepcopy(info)
            next_info.append(i)
            result.extend(get_all_type(r, next_info, lon))
    return result

Result = []
for i in get_all_type(R, [], r):
    j = deque(i)
    x = j.popleft()
    result = 0
    while j:
        y = j.popleft()
        result += wf[x][y]
        x = y
    Result.append(result)
print(min(Result))