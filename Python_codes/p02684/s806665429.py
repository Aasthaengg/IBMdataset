n, k = map(int, input().split())
a = list(map(int, input().split()))

route = []
town = set()
now = 1

while True:
    now = a[now-1]
    if now in town:
        break
    town.add(now)
    route.append(now)

count = route.index(now)
if count >= k:
    print(route[k-1])
else:
    route = route[count:]
    num = (k-count)%len(route)
    print(route[num-1])


    
