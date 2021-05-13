import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input())
edges = []
if N % 2 == 0:
    D = N+1
else:
    D = N
for i in range(1, D):
    for j in range(i+1, D):
        if i+j == D:
            continue
        else:
            edges.append(str(i)+" "+str(j))
if N % 2 == 1:
    for v in range(1, N):
        edges.append(str(v)+" "+str(N))
print(len(edges))
for e in edges:
    print(e)
