n,m = map(int,input().split())
h = [None] + list(map(int,input().split()))
road = [[] for _ in range(n+1)]
count = 0
for _ in range(m):
    a,b = map(int,input().split())
    road[a].append(b)
    road[b].append(a)
for i in range(1,n+1):
    max_hight = 0
    for j in road[i]:
        max_hight = max(max_hight, h[j])
    if h[i]>max_hight:
        count += 1

print(count)