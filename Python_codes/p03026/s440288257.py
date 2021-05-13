from collections import defaultdict, deque

N = int(input())
adj_list = defaultdict(list)
E = []
V_number = [None]*N
for _ in range(N-1):
    a, b = map(int, input().split())
    E.append((a, b))
    adj_list[a].append(b)
    adj_list[b].append(a)
C = sorted(list(map(int, input().split())), reverse=True)
q = deque([1])
i = 0
while q:
    v = q.popleft()
    V_number[v-1] = C[i]
    i += 1
    for u in adj_list[v]:
        if V_number[u-1] is None:
            q.append(u)

print(sum(C[1:]))
print(*V_number)