N, M = map(int, input().split())
Ne = [[] for _ in range(N)]
C = [0] * N
for i in range(M):
    A, B = map(int, input().split())
    Ne[A-1].append(B-1)
    Ne[B-1].append(A-1)
c=0
l = []
for i in range(N):
    if C[i] == 0:
        c+=1
        l.append(i)
        while len(l)>0:
            v=l.pop()
            C[v] = c
            for j in Ne[v]:
                if C[j] == 0:
                    l.append(j)
print(c-1)
