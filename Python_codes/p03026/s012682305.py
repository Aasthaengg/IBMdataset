from collections import deque
N = int(input())
T = [[] for i in range(N)]
for i in range(N-1):
    a,b = map(lambda x:int(x)-1,input().split())
    T[a].append(b)
    T[b].append(a)
P = list(map(int,input().split()))
P.sort(reverse=True)
A = [-1]*N
v = -1
for i in range(N):
    if len(T[i])==1:
        v = i
        break
Q = deque([v])
p_index = 0
while Q:
    v = Q.pop()
    A[v] = P[p_index]
    p_index+=1
    for c in T[v]:
        if A[c]==-1:
            Q.append(c)
print(sum(P[1:]))
print(*A)