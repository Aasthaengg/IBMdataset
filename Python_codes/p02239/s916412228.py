import collections

n=int(input())
adj=[]
for i in range(n):
      adj.append(list(map(int, input().split())))

Q=[]
Q=collections.deque()
Q.append(0)

D=[-1 for i in range(n)]
D[0]=0

while len(Q)>0:
    current=Q.popleft()
    for dst in range(n):
        for i in range(2,len(adj[current])):
            if adj[current][i]==dst+1 and D[dst]==-1:
                D[dst]=D[current]+1
                Q.append(dst)
for i in range(n):
    print(i+1,D[i])