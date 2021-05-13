from collections import defaultdict, deque
dic = defaultdict(list)
N, Q = map(int, input().split())
point = [0 for _ in range(N)]

for i in range(N-1):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

for _ in range(Q):
    p, x = map(int, input().split())
    point[p-1]+=x
    
queue = deque()
for i in dic[1]:
    queue.append(1)
    queue.append(i) #親、子
    
while queue:
    p = queue.popleft()
    c = queue.popleft()
    point[c-1]+=point[p-1] 
    
    for j in dic[c]:
        if j != p:
            queue.append(c)
            queue.append(j)
            
        
print(*point)
