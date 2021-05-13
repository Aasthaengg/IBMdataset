from queue import deque

n = int(input())
li = [[] for _ in range(n+1)]

for i in range(n-1):
    a,b = map(int,input().split())
    li[a] += [b]
    li[b] += [a]

def width_prime(start,li,n):
    inf = 10**10
    visited = [False]*(n+1)
    length = [inf]*(n+1)
    length[start] = 0
    visited[start] = True
    work_queue = deque([])
    work_queue.append(start)
    while work_queue:
        now = work_queue.popleft()
        visited[now] = True
        for i in li[now]:
            if visited[i]:
                continue
            work_queue.append(i)
            visited[i] = True
            if length[i] > length[now]+1:
                length[i] = length[now]+1
    return length

le_fe = width_prime(1,li,n)
le_su = width_prime(n,li,n)

su = 0
fe = 0
for i in range(1,n+1):
    if le_fe[i] <= le_su[i]:
        fe += 1
    else:
        su += 1

if fe > su:
    print("Fennec")
else:
    print("Snuke")