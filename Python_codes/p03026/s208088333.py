import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

c = list(map(int, input().split()))
c.sort(reverse = False)

tmp = len(graph[0])
start = 0
for index, x in enumerate(graph):
    if len(x) > tmp:
        tmp = len(x)
        start = index

ans = 0
ans_lst = [-1] * N
ans_lst[start] = c.pop()
stack = [start]
while stack:
    x = stack.pop()
    for next_ in graph[x]:
        if ans_lst[next_] == -1:
            tmp = c.pop()
            ans_lst[next_] = tmp
            stack.append(next_)
            ans += tmp

print (ans)
print (*ans_lst, sep = ' ')
