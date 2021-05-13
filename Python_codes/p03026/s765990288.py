n = int(input())

adj_list = [[] for _ in range(n)]

for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    adj_list[a].append(b)
    adj_list[b].append(a)

c = list(map(int, input().split()))
c.sort(reverse=True)
idx = 0

from collections import deque

dq = deque()

dq.append(0)
ans = [-1] * n

while len(dq) > 0:
    node = dq.popleft()
    ans[node] = c[idx]
    idx += 1
    for next_node in adj_list[node]:
        if ans[next_node] < 0:
            dq.append(next_node)

print(sum(c[1:]))
print(*ans)
