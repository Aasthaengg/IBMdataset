from collections import deque

n = int(input())
e = [[] for i in range(n)]
for i in range(n-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    e[a].append(b)
    e[b].append(a)
l = sorted(list(map(int,input().split())),reverse=True)
ans = [-1]*n

q = deque([])
q.append(0)
ans[0] = l[0]
now = 1
while q:
    b = q.popleft()
    for nex in e[b]:
        if ans[nex] == -1:
            ans[nex] = l[now]
            now += 1
            q.append(nex)
count = 0
for j in range(n):
    for k in e[j]:
        count += min(ans[j],ans[k])
print(count//2)
print(*ans)




