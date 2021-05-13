from collections import deque
N = int(input())
adj = [[] for i in range(N)]


for i in range(N-1):
    a, b = map(int, input().split())
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)


dq = deque([(0, 'b'), (N-1, 'w')])

colors = [0] * N
colors[0] = 'b'
colors[-1] = 'w'


while dq:
    node, color = dq.popleft()
    for dest in adj[node]:
        if colors[dest] != 0:
            continue
        else:
            colors[dest] = color
            dq.append((dest, color))

print('Fennec' if colors.count('b') > N//2 else 'Snuke')