import queue

N, M = map(int,input().split(' '))
#AB=[]
Root=[]
Sign=[]

for i in range(N+1):
    Root.append([])
    Sign.append(0)
#print(Root)

for i in range(M):
    a,b = map(int,input().split(' '))
    #AB.append([a,b])
    Root[a].append(b)
    Root[b].append(a)

q = queue.Queue()
q.put(1)

while not q.empty():
    r = q.get()
    for nextR in Root[r]:
        if Sign[nextR] == 0:
            q.put(nextR)
            Sign[nextR]=r

if 0 in Sign[1:]:
    print('No')
else:
    print('Yes')
    for i in range(2,N+1):
        print(Sign[i])
