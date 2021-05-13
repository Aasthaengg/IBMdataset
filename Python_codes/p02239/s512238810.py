import collections
n = int(input())
G = []
for i in range(n):
    T = [0]*n
    G.append(T)
for i in range(n):
    L = list(map(int,input().split()))
    for j in range(2,len(L)):
        G[i][L[j]-1] += 1
d = [float('inf')]*n
q = collections.deque()
q.append(0)
d[0] = 0
while len(q) > 0:
    start = q.popleft()
    for i in range(n):
        if G[start][i] == 1:
            if d[i] == float('inf'):
                q.append(i)
                d[i] = d[start]+1
for i in range(n):
    if d[i] != float('inf'):
        print(i+1,d[i])
    else:
        print(i+1,-1)
