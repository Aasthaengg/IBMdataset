from collections import deque

n = int(input())
Tree_dict = {}
for _ in range(n-1):
    a, b = map(int, input().split())
    if a in Tree_dict.keys():
        Tree_dict[a].append(b)
    else:
        Tree_dict.update({a:[b]})
    if b in Tree_dict.keys():
        Tree_dict[b].append(a)
    else:
        Tree_dict.update({b:[a]})

deque = deque()
deque.append(1)

Visited_one = [-1 for _ in range(n+1)]
Visited_one[1] = 0

while deque:
    node = deque.popleft()
    next_nodes = Tree_dict[node]
    for next_node in next_nodes:
        if Visited_one[next_node] != -1:
            continue
        else:
            Visited_one[next_node] = Visited_one[node] + 1
            deque.append(next_node)


deque.append(n)

Visited_n = [-1 for _ in range(n+1)]
Visited_n[n] = 0

while deque:
    node = deque.popleft()
    next_nodes = Tree_dict[node]
    for next_node in next_nodes:
        if Visited_n[next_node] != -1:
            continue
        else:
            Visited_n[next_node] = Visited_n[node] + 1
            deque.append(next_node)

# print(Visited_one)
# print(Visited_n)

fen = 0
snu = 0

for i in range(1,n+1):
    if Visited_n[i] >= Visited_one[i]:
        fen += 1
    else:
        snu += 1

if fen > snu:
    ans = 'Fennec'
else:
    ans = 'Snuke'
print(ans)