from collections import deque

N = int(input())
E = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    E[a-1].append(b-1)
    E[b-1].append(a-1)
    
q = deque()
q.append(0)
parents = [-1]*N
parents[0] = -2
while q:
    t = q.popleft()
    for i in E[t]:
        if parents[i] == -1:
            parents[i] = t
            q.append(i)
    if parents[N-1] >= 0:
        break

q_snuke = deque()
q_snuke.append(N-1)
idx = N-1
used = [0]*N
used[0] = 1
cnt = 0
while parents[idx] >= 0:
    q_snuke.append(parents[idx])
    idx = parents[idx]
    used[idx] = 1

n = len(q_snuke)
for _ in range(n//2+(n%2)):
    q_snuke.pop()
    

while q_snuke:
    t = q_snuke.popleft()
    for i in E[t]:
        if used[i] == 0:
            used[i] = 1
            q_snuke.append(i)

s = sum(used) - (n//2+(n%2))
if s >= N-s or N == 2:
    print("Snuke")
else:
    print("Fennec")