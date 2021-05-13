n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)
c = [int(i) for i in input().split()]
c.sort()
c.reverse()
ans_list = [0 for _ in range(n)]
ans = 0
p_list = [0]
ans_list[0] = c.pop(0)
while len(p_list) > 0:
    p = p_list.pop(0)
    for g in graph[p]:
        if ans_list[g] == 0:
            ans_list[g] = c.pop(0)
            ans += ans_list[g]
            p_list.append(g)
print(ans)
print(' '.join([str(i) for i in ans_list]))