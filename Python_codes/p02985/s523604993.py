from collections import deque
N, K = map(int, input().split())
ab = [list(map(int,input().split())) for _ in range(N-1)]
mod = 1000000007

routes = [[] for _ in range(N)]
for i in range(N-1):
    routes[ab[i][0]-1].append(ab[i][1]-1)
    routes[ab[i][1]-1].append(ab[i][0]-1)

options = [0 for i in range(N)]
seen = [False for _ in range(N)]
options[0] = K
seen[0] = True
todo = deque([0])
color = 0
while len(todo):
    checking = todo.pop()
    if checking == 0:
        rest = K
    else:
        rest = K-1
    for route in routes[checking]:
        if seen[route] == False: 
            todo.append(route)
            rest = rest - 1
            options[route] = rest
            seen[route] = True

answer = 1
for i in range(N):
    answer = (answer * options[i])%mod
print(answer)