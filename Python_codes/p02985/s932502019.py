import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, K = map(int, readline().split())
MOD = 10 ** 9 + 7
#AB = [[int(x) - 1 for x in readline().split()] for _ in range(N-1)]

PATH = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, readline().split())
    PATH[a].append(b)
    PATH[b].append(a)

# print("hoge")
DONE = [False] * (N+1)

ans = K
q = [(1, 0)]
while q:
    u, cnt = q.pop()
    DONE[u] = True
    i = 0
    for v in PATH[u]:
        if u == v or DONE[v]:
            continue
        ans *= K - i - 1 - cnt
        ans %= MOD
        q.append((v, 1))
        i += 1


print(ans)
