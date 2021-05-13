n = int(input())
a = [[] for i in range(n)]

for i in range(n):
    v = list(map(int, input().split()))
    u = v[0] - 1
    for j in v[2:]:
        a[u].append(j-1)

d = [-1] * n
isDiscovered = [False] * n

def bfs(x):
    for i in a[x]:
        if not isDiscovered[i]:
            isDiscovered [i] = True
            d[i] = d[x] + 1

d_ = 0
isDiscovered [0] = True
d[0] = 0
bfs(0)

flag = True
while flag:
    flag = False
    for i in range(n):
        if d[i] is d_ :
            flag = True
            bfs(i)
    d_ += 1

for i in range(n):
    print(i+1, d[i])