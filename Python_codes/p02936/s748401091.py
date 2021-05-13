n, q = map(int, input().split())
li_nq = [list(map(int, input().split())) for _ in range(n-1)]
li_px = [list(map(int, input().split())) for _ in range((q))]

graph = [[] for _ in range(n+1)]
for i, j in li_nq:
    graph[i].append(j)
    graph[j].append(i)

ans = [0 for _ in range(n+1)]
for i, j in li_px:
    ans[i] += j

check_list = [None] * (n+1)
stack = [1]

while stack:
    num = stack.pop()
    for i in graph[num]:
        if check_list[num] == i:
            continue
        stack.append(i)
        ans[i] += ans[num]
        check_list[i] = num

print(*ans[1:])