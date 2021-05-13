n,m = map(int,input().split())
l = [[] for i in range(n)]

for i in range(m):
    a,b = map(int,input().split())
    l[a-1].append(b-1)
    l[b-1].append(a-1)

mp = [False]*n
mcnt = 0
for i in range(n):
    if mp[i]:
        continue
    queue = [i]
    cnt = 0
    mp[i] = True
    while(queue):
        num = queue.pop()
        cnt += 1
        target = set(l[num])
        for x in target:
            if mp[x]:
                continue
            mp[x]=True
            queue.append(x)
    mcnt = max(cnt,mcnt)

print(mcnt)
