N, u, v = map(int,input().split())
u, v = u - 1, v - 1
path = [] 
for _ in range(N):
    path.append([])
for _ in range(N - 1):
    A, B = map(int,input().split())
    A, B = A - 1, B - 1
    path[A].append(B)
    path[B].append(A)
dep = [0] * N
dep[v] = 1
leaf = []
stack2 = [v]
cnt = 2
while stack2:
    stack = stack2[0:]
    stack2 = []
    while stack:
        s = stack.pop()
        for to in path[s]:
            judge = len(path[s])
            if dep[to]:
                judge -= 1
                if judge == 0:
                    leaf.append([cnt - 1, s])
                continue
            dep[to] = cnt
            stack2.append(to)
            judge += 1 
    cnt += 1
leaf.sort(reverse=True)
depmax = [0] * N
for i in range(len(leaf)):
    depth, a = leaf[i][0], leaf[i][1] 
    depmax[a] = depth
    end = False
    for j in range(depth - 1, 0, -1):
        if end:
            break
        for b in path[a]:
            if dep[b] == j:
                if depmax[b] < depmax[a]:
                    depmax[b] = depmax[a]
                    a = b
                    break
                else:
                    end = True
                    break
dis = dep[u] - 2
leng = depmax[u]
a = u
for depth in range(dep[u] - 1, dep[u] - 1 - (dis // 2), -1):
    for to in path[a]:
        if depth == dep[to]:
            leng = depmax[to]
            a = to
print(leng - 2)