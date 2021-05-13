def abc126d():
    n = int(input())
    e = [list() for _ in range(n)]
    for _ in range(n-1):
        u, v, w = map(int, input().split())
        e[u - 1].append([v - 1, w])
        e[v - 1].append([u - 1, w])
    ans = [-1] * n
    ans[0] = 0
    q = e[0].copy()
    while len(q) > 0:
        v, w = q.pop()
        #print(v, w)
        if ans[v] != -1: continue
        elif w % 2 == 0: ans[v] = 0
        else: ans[v] = 1
        for v1, w1 in e[v]:
            if ans[v1] != -1: continue
            q.append([v1, w+w1])
    for i in ans:
        print(i)
abc126d()