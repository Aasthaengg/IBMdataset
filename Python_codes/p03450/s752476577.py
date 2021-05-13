import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    L, R, D = map(int, input().split())
    graph[L].append((R, D))
    graph[R].append((L, -D))

d = [None] * (N + 1)

def calc(start): #startからの連結成分をチェックする
    d[start] = 0
    stack = [start]
    while len(stack) != 0:
        tmp = stack.pop()
        for next_, diff in graph[tmp]:
            if d[next_] == None:
                d[next_] = d[tmp] + diff
                stack.append(next_)
            else:
                if d[next_] == d[tmp] + diff:
                    pass
                else:
                    print ('No')
                    exit()
    return 

# for i in graph:
#     print (i)

for i in range(1, N):
    if d[i] == None:
        calc(i)
print ('Yes')
