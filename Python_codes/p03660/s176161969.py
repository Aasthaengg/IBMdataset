from collections import deque

N = int(input())

data = [[] for i in range(N)]

for i in range(N-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    data[a].append(b)
    data[b].append(a)

stack = deque([0])
visit_in = [-1]*N
visit_in[0] = 0

while stack:
    x = stack.pop()
    for y in data[x]:
        if visit_in[y] >= 0:
            continue
        visit_in[y] = x
        stack.append(y)

path = [N-1]

while path[-1] != 0:
    path.append(visit_in[path[-1]])

#print(path)

group = [-1]*N

for x in path:
    group[x] = x

stack = deque(path[:])

while stack:
    x = stack.pop()
    for y in data[x]:
        if group[y] != -1:
            continue
        group[y] = group[x]
        stack.append(y)

#print(group)

num = [0]*N
for i in range(N):
    num[group[i]] += 1

#print(num)

p = len(path)-1
q = 0
fennec = num[0]
snuke = num[N-1]
#print(fennec,snuke)
while q < p - 1:
    p -= 1
    fennec += num[path[p]]
    if q < p -1:
        q += 1
        snuke += num[path[q]]
    #print(fennec,snuke)
    

if fennec <= snuke:
    print("Snuke")
else:
    print("Fennec")