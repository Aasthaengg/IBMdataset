n, m = map(int, input().split())
n -= 1

l = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    l[a].append(b)
    l[b].append(a)

if len(l[n]):
    for x in l[n]:
        if l[x].count(0):
            print('POSSIBLE')
            exit()
print('IMPOSSIBLE')