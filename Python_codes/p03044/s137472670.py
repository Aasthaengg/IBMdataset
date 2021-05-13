from _collections import deque
N = int(input())
T = [[] for _ in range(N)]
for i in range(N-1):
    u,v,w = map(int,input().split())
    T[u-1].append([v-1,w%2])
    T[v-1].append([u-1,w%2])

ans = [0]*N
used_1 = [0]*N
used_2 = [0]*N
for i in range(N):
    if used_1[i] == 0:
        used_1[i] = 1
        u = i
        P = deque([])
        for j in range(len(T[i])):
            v = T[u][j][0]
            w = T[u][j][1]
            P.append(v)
            if used_2[v] == 1:
                k = ans[v]
                if k == 1:
                    if w == 1:
                        ans[u] = 0
                    else:
                        ans[u] = 1
                else:
                    if w == 1:
                        ans[u] = 1
                    else:
                        ans[u] = 0
                used_2[u] = 1
            elif used_2[u] == 1:
                k = ans[u]
                if k == 1:
                    if w == 1:
                        ans[v] = 0
                    else:
                        ans[v] = 1
                else:
                    if w == 1:
                        ans[v] = 1
                    else:
                        ans[v] = 0
                used_2[v] = 1
            else:
                if w == 1:
                    ans[v] = 1
                else:
                    pass
                used_2[u] = 1
                used_2[v] = 1
        while(True):
            i = P.popleft()
            if used_1[i] == 0:
                used_1[i] = 1
                u = i
                for j in range(len(T[i])):
                    v = T[u][j][0]
                    w = T[u][j][1]
                    P.append(v)
                    if used_2[v] == 1:
                        k = ans[v]
                        if k == 1:
                            if w == 1:
                                ans[u] = 0
                            else:
                                ans[u] = 1
                        else:
                            if w == 1:
                                ans[u] = 1
                            else:
                                ans[u] = 0
                        used_2[u] = 1
                    elif used_2[u] == 1:
                        k = ans[u]
                        if k == 1:
                            if w == 1:
                                ans[v] = 0
                            else:
                                ans[v] = 1
                        else:
                            if w == 1:
                                ans[v] = 1
                            else:
                                ans[v] = 0
                        used_2[v] = 1
                    else:
                        if w == 1:
                            ans[v] = 1
                        else:
                            pass
                        used_2[u] = 1
                        used_2[v] = 1
            if len(P) == 0:
                break

for i in ans:
    print(i)