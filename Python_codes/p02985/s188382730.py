import collections, queue, sys
n, k =  map(int, input().split())
m = 10**9+7
edges = collections.defaultdict(list)
q = queue.Queue()
preq = queue.Queue()
ans = 1

for i in range(n-1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

j = 1
for i in edges[1]:
    q.put(i)
    preq.put(1)
    if k - j <= 0:
        print(0)
        sys.exit()
    ans = ans%m * (k - j)%m
    j+=1

while not q.empty():
    j = 2
    node = q.get()
    prenode = preq.get()
    for i in edges[node]:
        if not i == prenode:
            q.put(i)
            preq.put(node)
            if k - j <= 0:
                print(0)
                sys.exit()
            ans = ans%m * (k - j)%m
            j+=1
print((ans*k)%m)
