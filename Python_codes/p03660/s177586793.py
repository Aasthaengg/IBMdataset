from collections import deque
import sys
sys.setrecursionlimit(10**8)
n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    graph[a].append(b)
    graph[b].append(a)
fennec = [10**5 + 10] * n
fennec[0] = 0
snuke = [10**5 + 10] * n
snuke[n - 1] = 0


def bfs(arr, q):
    while len(q) > 0:
        nex_q = []
        for qq in q:
            for nex in graph[qq[0]]:
                if arr[nex] > qq[1] + 1:
                    arr[nex] = qq[1] + 1
                    nex_q.append([nex, arr[nex]])
        q = nex_q[:]


sq, gq = deque(), deque()
sq.append([0, 0])
gq.append([n - 1, 0])
bfs(fennec, sq)
bfs(snuke, gq)
ans = 0
for i in range(n):
    if fennec[i] <= snuke[i]:
        ans += 1
    else:
        ans -= 1
# なんでans=>0じゃないん？？？？？？？？？？？？？？？？？？
# > 手番のプレイヤーがマスに色を塗ることができなかったとき、敗者となります。
# あー総合の数じゃなかったわ...
print("Fennec" if ans > 0 else "Snuke")
