from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())

graph = [[] for i in range(N)]

for i in range(M):
    L,R,D = map(int,input().split())
    L -= 1
    R -= 1
    graph[L].append([R,D])
    graph[R].append([L,-D])
    
data = [None]*N

for i in range(N):
    if data[i] != None:
        continue
    data[i] = 0
    stack = deque()
    stack.append(i)
    while stack:
        x = stack.popleft()
        for y in graph[x]:
            if data[y[0]] == None:
                data[y[0]] = data[x] + y[1]
                stack.append(y[0])
            else:
                if data[y[0]] - data[x] != y[1]:
                    print("No")
                    sys.exit()
    
print("Yes")

