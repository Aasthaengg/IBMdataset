import queue
n = int(input())

abc = [[] for i in range(n+1)]

for i in range(n-1):
    a,b,c = map(int,input().split())
    abc[a].append([b,c])
    abc[b].append([a,c])

Q,k = map(int,input().split())
xy = [[int(i) for i in input().split()] for j in range(Q)]

q = queue.Queue()

q.put(k)

path = [-1]*(n+1)
path[k] = 0

while not q.empty():
    tmp = q.get()
    for i in range(len(abc[tmp])):
        #print(abc[tmp])
        #exit()
        num = abc[tmp][i][0]
        if path[num] != -1:
            continue
        else:
            path[num] = path[tmp] + abc[tmp][i][1]
            q.put(num)
            
for i in range(Q):
    print(path[xy[i][0]]+path[xy[i][1]])