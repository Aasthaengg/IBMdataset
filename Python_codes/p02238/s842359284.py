from collections import deque
time = 1

def dfs(adj_list, d, f, color, u):

    global time
    S = list()

    S.append(u)
    color[u] = "G"
    d[u] = time
    time += 1

    while len(S) != 0:
        u = S[-1]

        if len(adj_list[u]) != 0:
            v = adj_list[u].popleft()

            if color[v] == "W":
                color[v] = "G"
                d[v] = time
                time += 1
                S.append(v)
        else:
            S.pop()
            color[u] = "B"
            f[u] = time
            time += 1

def Main():
    
    N = int(input())
    adj_list = [deque() for n in range(N)]
    d = [0] * N
    f = [0] * N
    color = [ "W" for i in range(len(d)) ]

    for n in range(N):
        u, k, *V = map(int, input().split())

        if k > 0:
            for i in V:
                adj_list[n].append(i - 1)

    while(True):

        ind = None
        for i in range(N):
            if color[i] == "W":
                ind = i
                break

        if ind == None:
            break
        else:
            dfs(adj_list, d, f, color, ind)

    for i in range(N):
        print("{} {} {}".format(i + 1, d[i], f[i] ))

Main()
