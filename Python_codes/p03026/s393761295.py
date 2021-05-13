import sys
sys.setrecursionlimit(10**7)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def MI(): return map(int, sys.stdin.readline().split())
def II(): return int(sys.stdin.readline())


def func(v):
    if ans[v] != -1:
        return
    ans[v] = c[index]
    global index
    index += 1
    for next_v in graph[v]:
        if v == next_v:
            continue
        func(next_v)


n = II()
graph = [[] for _ in range(n)]
for _ in range(n-1):
    u, v = MI()
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)
c = sorted(LI(), reverse=True)
ans = [-1] * n
index = 0
func(0)
print(sum(c[1::]))
for i in range(n):
    print(ans[i], end=' ')
print()
