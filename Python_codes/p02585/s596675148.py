import sys
input = sys.stdin.buffer.readline

n,k = map(int,input().split())
p = list(map(int,input().split()))

for i in range(n):
    p[i] -= 1

c = list(map(int,input().split()))
used = [False]*n

edge = []

for i in range(n):
    if used[i]:
        continue
    now = i
    edge.append([])

    while True:
        if used[now]:
            break
        used[now] = True
        edge[-1].append(c[now])
        now = p[now]

res = -10**9
for i in range(len(edge)):
    s = sum(edge[i])
    m = len(edge[i])

    for j in range(m):
        tmp = 0
        ctr = 0
        for h in range(j+1,m):
            ctr += 1
            tmp += edge[i][h]
            if ctr <= k:
                res = max(res,tmp,tmp+((k-ctr)//m)*s)
        for h in range(j+1):
            ctr += 1
            tmp += edge[i][h]
            if ctr <= k:
                res = max(res,tmp,tmp+((k-ctr)//m)*s)
print(res)