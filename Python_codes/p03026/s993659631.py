import numpy as np 
N = int(input())
# N = 1000
# G = np.zeros((N,N),dtype = np.bool)

linked = [[] for i in range(N)]
pairs = []

for i in range(N-1):
    a,b = map(int,input().split())
    # a,b = 1,2
    pairs.append((a,b))
    linked[a-1].append(b-1)
    linked[b-1].append(a-1)

Cs = list(sorted(map(int,input().split()),reverse=True))
# Cs = [1 for i in range(N)]

# print(Cs)

links = np.array([0 for i in range(N)])

for i in range(N):
    links[i] = len(linked[i])

# minag = np.argmin(links)
nodeval = np.array([0 for i in range(N)])

stack = [1]

visited = [False for i in range(N)]

while(len(stack)>0):
    minag = stack.pop()
    nodeval[minag] = Cs.pop(0)
    for l in linked[minag]:
        if not visited[l]:
            stack.append(l)
    visited[minag] = True
    # print(nodeval)

sumval=0
for p in pairs:
    sumval += min(nodeval[p[0]-1], nodeval[p[1]-1] )

print(sumval)
for i,l in enumerate(nodeval):
    print(l,end=" " if i!=N-1 else "\n")
