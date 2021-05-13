import sys
input = sys.stdin.buffer.readline

from collections import deque

N = int(input())
neighbor = [[] for _ in range(N)]

for _ in range(N-1):
    a, b = map(int, input().split())
    neighbor[a-1].append(b-1)
    neighbor[b-1].append(a-1)

c = list(map(int, input().split()))
c.sort(reverse = True)

d = deque([0])
ans = [c[0]] + [0]*(N-1)
M = 0
c_idx = 1

while d:
    p = d.popleft()
    for n in neighbor[p]:
        if not ans[n]:
            ans[n] = c[c_idx]
            M += c[c_idx]
            c_idx += 1
            d.append(n)

print(M)
print(*ans)