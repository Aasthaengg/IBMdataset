N, K = list(map(int, input().split()))
A = [0] + list(map(int, input().split()))

path = [0]*(N+1)
visited = set()

pos = 1
for i in range(N+1):
    if pos in visited: break
    path[i] = pos
    visited.add(pos)
    pos = A[pos]

loc = path.index(pos)
head = path[:loc]
rep = path[loc:i]

if K < len(head):
    print(head[K])
else:
    print(rep[(K - len(head)) % len(rep)])

