n,k = map(int,input().split())
if n == 1:
    print(k)
else:
    edges = {}
    for i in range(n-1):
        a,b = map(int,input().split())
        if a not in edges:
            edges[a] = [b]
        else:
            edges[a].append(b)

        if b not in edges:
            edges[b] = [a]
        else:
            edges[b].append(a)

    now = set([1])
    visited = set([1])
    goal = -1
    flag = False
    ans = k
    mod = 10**9+7
    while True:
        buf = set()
        if len(now) == 0:
            break
        for n in now:
            if n == 1:
                for i in range(len(edges[n])):
                    ans *= k-1-i
                    ans %= mod
                for nn in edges[n]:
                    if nn in visited:
                        continue
                    else:
                        buf.add(nn)
                        visited.add(nn)

            else:
                temp = 0
                for nn in edges[n]:
                    if nn in visited:
                        continue
                    else:
                        temp += 1
                        buf.add(nn)
                        visited.add(nn)
                for i in range(temp):
                    ans *= k - 2 - i
                    ans %= mod
        # print(buf)
        # print(ans)
        now = buf
    # print(visited)
    print(ans%mod)

    # def tree_bfs(start,goal,edges):
    #     now = set([start])
    #     visited = set([start])
    #     flag = False
    #     while True:
    #         buf = set()
    #         if len(now) == 0:
    #             break
    #         for n in now:
    #             for nn in edges[n]:
    #                 if nn in visited:
    #                     continue
    #                 else:
    #                     buf.add(nn)
    #                     visited.add(nn)
    #
    #                 if nn == goal:
    #                      flag =True
    #                      break
    #         if flag:
    #             break
    #         else:
    #             now = buf