def find(x):
    while x!=T[x][0]:
        x = T[x][0]
    return x
def union(x,y):
    rt1 = find(x)
    rt2 = find(y)
    if T[rt1][1]>=T[rt2][1]:
        T[rt2][0] = rt1
        T[rt1][1] += T[rt2][1]
    else:
        T[rt1][0] = rt2
        T[rt2][1] += T[rt1][1]
N,M = map(int,input().split())
E = [list(map(int,input().split())) for _ in range(M)]
T = {i:[i,1] for i in range(1,N+1)}
RT = {i:1 for i in range(1,N+1)}
cnt = 0
ans = (N*(N-1))//2
A = []
A.append(ans)
for i in range(M-1,-1,-1):
    a,b = E[i]
    rt1 = find(a)
    rt2 = find(b)
    if rt1==rt2:
        A.append(ans)
    else:
        x = T[rt1][1]
        y = T[rt2][1]
        ans += (x*(x-1))//2+(y*(y-1))//2
        union(a,b)
        rt = find(a)
        z = T[rt][1]
        ans -= (z*(z-1))//2
        A.append(ans)
A = A[::-1]
for i in range(1,M+1):
    print(A[i])