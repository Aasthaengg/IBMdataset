#連結グラフではない
n = int(input())
V = [[] for _ in range(n+1)]
for _ in range(n):
    inpt = list(map(int,input().split( )))
    if len(inpt)>2:
        V[inpt[0]] = inpt[2:]


D = [0]*(n+1)
F = [0]*(n+1)

time = 1
Q = [1]
D[0] = -1
D[1] = 1
while len(Q) > 0 or 0 in D[1:]:
    v = Q[-1]
    remains = False
    for i in V[v]:
        if D[i] == 0:
            D[i] = time+1
            Q.append(i)
            remains = True
            break
    if not remains:
        F[v] = time+1
        Q.pop()
        
    time += 1
    if len(Q) == 0:
        if 0 in D:
            time += 1
            nxt = D.index(0)
            Q.append(nxt)
            D[nxt] = time
        else:
            pass
        

for i in range(1,n+1):
    print(i,D[i],F[i])

