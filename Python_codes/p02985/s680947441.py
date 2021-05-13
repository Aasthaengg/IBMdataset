from collections import deque
n,k = map(int,input().split())
l = [[] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    l[a].append(b)
    l[b].append(a)
rl = [0 for i in range(n+1)]
nl = [0 for i in range(n+1)]
ans = 0
nl[0] = -1
d = deque()
d.append([1,0])
rl2 = [0 for i in range(n+1)]
rl2[0] = 1
while len(d):
    [now,p] = d.popleft()
    #print(rl,nl,now,p)
    rl[now] = k - nl[p] - 1
    nl[p] += 1
    rl2[now] = 1
    if now != 1:
        nl[now] += 1
    for i in l[now]:
        if rl2[i] == 0:
            d.append([i,now])
ans = 1
mod = 10**9+7
#print(l,rl,nl)
for i in range(1,n+1):
    ans *= rl[i]
    ans %= mod
if ans > 0:
    print(ans)
else:
    print(0)