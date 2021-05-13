N, K = map(int, input().split())
inf = 10**18
sushi = [[-inf] for _ in range(N)]
for i in range(N):
    t, d = map(int, input().split())
    sushi[t-1].append(d)
for i in range(N):
    sushi[i].sort(reverse = True)
sushi.sort(key = lambda x:x[0], reverse = True)
que = []
res = 0
for i in range(K):
    res+=sushi[i][0]
    for j in sushi[i][1:]:
        que.append(j)
que.sort()
cur = res
res+=K**2
for var in range(1, K)[::-1]:
    a = que.pop()
    b = sushi[var][0]
    cur+=a-b
    res = max(res, cur+var**2)
print(res)


