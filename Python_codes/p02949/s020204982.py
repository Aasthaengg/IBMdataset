from collections import deque
import sys
input = sys.stdin.readline
inpl = lambda: list(map(int,input().split()))

def bellman_ford(start, goal, N, edges,
                 get_route=False,
                 negative_loop=None,
                 start_distance=0,
                 plus_func=lambda D,d: D+d):
    '''
    goal: int or list or set
    edges: list or dict
        edges[x] = {(y0, distance0), ...}
    '''
    distance = [None]*N
    predecessor = [None]*N
    if isinstance(goal, int):
        goal = [goal]
    elif isinstance(goal, set):
        goal = list(goal)
    M = len(goal)
    goalable = [[False]*N for _ in range(M)]
    for m in range(M):
        goalable[m][goal[m]] = True
    distance[start] = start_distance
    for _ in range(N-1):
        for i in range(N):
            if distance[i] is None:
                continue
            for j, d in edges[i]:
                for m in range(M):
                    if goalable[m][j]:
                        goalable[m][i] = True
                p = plus_func(distance[i], d)
                if distance[j] is None or distance[j] > p:
                    distance[j] = p
                    predecessor[j] = i

    goal_valid = [True]*M
    for i in range(N):
        if distance[i] is None:
            continue
        for j, d in edges[i]:
            if distance[j] is not None and plus_func(distance[i], d) < distance[j]:
                # Negative loop detected.
                for m in range(M):
                    if goal_valid[m] and goalable[m][i]:
                        distance[goal[m]] = negative_loop
                        goal_valid[m] = False
    if get_route:
        return distance, predecessor
    else:
        return distance

N, M, P = inpl()
uv = [ set() for _ in range(N) ]
for i in range(M):
    a, b, c = inpl()
    a -= 1
    b -= 1
    uv[a].add((b,-c+P))

distance = bellman_ford(0, N-1, N, uv)
minus_ans = distance[-1]
if minus_ans is None:
    print(-1)
elif minus_ans > 0:
    print(0)
else:
    print(-minus_ans)
