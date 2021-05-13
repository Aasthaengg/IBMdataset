N = int(input())
G = {i:[] for i in range(1,N+1)}
A = list(map(int,input().split()))
A.insert(0,0)
A.insert(0,0)
for i in range(2,N+1):
    G[A[i]].append(i)
for i in range(1,N+1):
    print(len(G[i]))