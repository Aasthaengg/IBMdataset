import sys
sys.setrecursionlimit(10 ** 6)

from collections import deque



def submit():
    n = int(input())
    edge = {i: [] for i in range(1, n + 1)}
    for _ in range(n - 1):
        a, b = map(int, input().split())
        edge[a].append(b)
        edge[b].append(a)

    # 1とNの最短路を求める
    def dfs(q, path, hist):
        p = q.pop()
        if p == n:
            return path

        for e in edge[p]:
            if not hist[e]:
                q.append(e)
                path.append(e)
                hist[e] = True
                ret = dfs(q, path, hist)
                if ret:
                    return ret
                path.pop(-1)
        return None


    q = deque()
    q.append(1)
    hist = {i: False for i in range(n + 1)}
    hist[1] = True
    direct_path = dfs(q, [1], hist)
    d = len(direct_path) 
    if d % 2:
        fennec = direct_path[:d // 2 + 1]
        snuke = direct_path[d // 2 + 1:]
    else:
        fennec = direct_path[:d // 2]
        snuke = direct_path[d // 2:]

    edge[fennec[-1]].remove(snuke[0])
    
    # fennecが取れる数を数える
    color = 0
    picked = [False for _ in range(n)]
    q = deque()
    q.append(1)
    picked[0] = True
    while len(q):
        p = q.pop()
        color += 1
        for e in edge[p]:
            if not picked[e - 1]:
                q.append(e)
                picked[e - 1] = True
    
    if color > n - color:
        print("Fennec")
    else:
        print("Snuke")


submit()