from collections import deque

n = int(input())
t = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    t[a].append(b)
    t[b].append(a)
c = sorted(list(map(int, input().split())))

queue = deque([0])
ans = [0 for i in range(n)]
num = n - 1
while queue:
    cur_node = queue.popleft()
    if ans[cur_node] > 0:
        continue
    ans[cur_node] = c[num]
    num -= 1
    for i in t[cur_node]:
        queue.append(i)
print(sum(c) - max(c))
print(*ans)