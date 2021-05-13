from collections import deque

N = int(input())
dic = {}
lnum = [0] * N
q = deque([])
alis = [0] * N


for i in range(N-1):

    a,b = map(int,input().split())
    a -= 1
    b -= 1

    lnum[a] += 1
    lnum[b] += 1

    if a not in dic:
        dic[a] = []

    if b not in dic:
        dic[b] = []

    dic[a].append(b)
    dic[b].append(a)

for i in range(N):

    if lnum[i] == 1:
        q.append(i)

c = list(map(int,input().split()))
c.sort()
#print (c)
for i in range(N):

    now = q.popleft()
    lnum[now] = 0

    alis[now] = c[i]
    #print (q,now,alis)

    for nex in dic[now]:

        lnum[nex] -= 1
        if lnum[nex] == 1:
            q.append(nex)

print (sum(c) - c[-1])
print (" ".join(map(str,alis)))
