import sys
readline = sys.stdin.readline

def topological_sort(E, D):
    D = D[:]
    n = len(E)
    Q = [i for i in range(n) if D[i] == 0]
    L = []
    while Q:
        p = Q.pop()
        L.append(p)
        for vf in E[p]:
            D[vf] -= 1
            if not D[vf]:
                Q.append(vf)
    
    if len(L) != n:
        return False
    return L

def check(E, D, N):
    D = D[:]
    Q = [i for i in range(N**2) if D[i] == 0 and i//N < i%N]
    
    cnt = 0
    res = 0
    match = N*(N-1)//2
    while match > res:
        cnt += 1
        res += len(Q)
        Q2 = []
        for q in Q:
            for vf in Edge[q]:
                D[vf] -= 1
                if not D[vf]:
                    Q2.append(vf)
        Q = Q2[:]
    return cnt
        
N = int(readline())
AA = [list(map(lambda x:int(x)-1, readline().split())) for _ in range(N)]

Edge = [[] for _ in range(N**2)]
Dim = [0]*(N**2)
for i in range(N):
    for j in range(N-2):
        noden = min(i, AA[i][j]) * N + max(i, AA[i][j])
        nodef = min(i, AA[i][j+1]) * N + max(i, AA[i][j+1])
        Dim[nodef] += 1
        Edge[noden].append(nodef)
L = topological_sort(Edge, Dim)
if L == False:
    ans = -1
else:
    ans = check(Edge, Dim, N)
print(ans)
