from collections import defaultdict, deque
import sys
sys.setrecursionlimit(10**9)


N, Q = map(int, input().split())
count = [0] * N
parent = defaultdict(int)
t = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    t[a - 1].append(b)
    t[b - 1].append(a)

for i in range(Q):
    p, x = map(int, input().split())
    count[p - 1] += x


f = [False] * N
q = deque([1])
while(q):
    n = q.popleft()
    f[n-1] = True
    for i in t[n-1]:
        if f[i-1]:
            continue
        q.append(i)
        count[i-1]+=count[n-1]
        f[i-1] = True
#for i in range(1, N):
#    count[i] += count[parent[i + 1] - 1]
#print(parent)
print(*count)
