from collections import defaultdict
from collections import deque
dic = defaultdict(set)
n = int(input())
for i in range(n-1):
    a, b = map(int, input().split())
    dic[a].add(b)
    dic[b].add(a)
q = deque([(1, 'F'), (n, 'S')])
seen = set([1, n])
f = 1
s = 1
while q:
    p, player = q.popleft()
    for child in dic[p]:
        if child not in seen:
            seen.add(child)
            q.append((child, player))
            if player == 'F':
                f += 1
            else:
                s += 1
print('Fennec' if f > s else 'Snuke')
