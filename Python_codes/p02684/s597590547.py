n, k = map(int, input().split())
a = list(map(int, input().split()))
alr = [0 for i in range(n)]
now = 1
path = [now]

for i in range(k):
    now = a[now-1]
    # if now in path:
    #     now = path[path.index(now) + (k-i-1)%(len(path) - path.index(now))]
    #     break
    if alr[now-1] != 0:
        now = path[path.index(now) + (k-i-1)%(len(path) - path.index(now))]
        break
    path.append(now)
    alr[now-1] += 1

print(now)
