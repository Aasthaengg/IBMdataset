#B - Counting Roads
N,M = map(int,input().split())
a = []
b = []
for _ in range(M):
    ai,bi = map(int,input().split())
    a.append(ai)
    b.append(bi)
start = a + b
count = [0]*N
for i in range(len(start)):
    count[start[i]-1] += 1
    
for o in range(N):
    print(count[o])