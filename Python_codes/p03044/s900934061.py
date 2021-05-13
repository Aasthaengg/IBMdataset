import sys
input = sys.stdin.readline
from collections import deque
def bfs(now):
    plan = deque()
    plan.append(now)
    while plan:
        now = plan.popleft()
        color = COLOR[now]
        for bady, l in LINK[now]:
            if COLOR[bady] != -1:
                continue
            plan.append(bady)
            if l%2:
                COLOR[bady] = 1 - color
            else:
                COLOR[bady] = color

if __name__ == '__main__':
    N = int(input())
    LINK = [[]*(N+1) for i in range(N+1)]
    # LINK = [deque()*(N+1) for i in range(N+1)]
    for i in range(N-1):
        a, b, l = map(int, input().split())
        LINK[a].append([b, l])
        LINK[b].append([a, l])
    # print(LINK)
    # print(LINK[1])
    # print(LINK[1][0])
    COLOR= [-1]*(N+1)
    COLOR[1] = 1
    bfs(1)
    for i in range(1,N+1):
        print(COLOR[i])