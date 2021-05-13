import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

N = int(input())
edge = [[] for _ in range(N + 1)]
AB = []
for _ in range(N - 1):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)
    AB.append((a, b))
C = list(map(int, input().split()))
C.sort()

for i, e in enumerate(edge[1:], start=1):
    if len(e) == 1:
        s = i
        break

node = [s]
memo = [-1] * (N + 1)
while node:
    s = node.pop()
    memo[s] = C.pop()
    for t in edge[s]:
        if memo[t] != -1:
            continue
        node.append(t)

ans = 0
for a, b in AB:
    ans += min(memo[a], memo[b])

print(ans)
print(*memo[1:])
