from collections import deque
N, Q = list(map(int, input().split()))
S = [set() for _ in range(N)]
for _ in range(N-1):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    S[a].add(b)
    S[b].add(a)
node = [0]*N
for _ in range(Q):
    t, v = list(map(int, input().split()))
    t -= 1
    node[t] += v

seen = [False]*N
stk = deque([(0, 0)])
while stk:
    t, v = stk.pop()
    seen[t] = True
    node[t] += v
    s = S[t]
    for k in s:
        if not seen[k]:
            stk.appendleft((k, node[t]))
print(*node)
