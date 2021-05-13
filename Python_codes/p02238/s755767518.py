n = int(input())
a = [[] for i in range(n)]

for i in range(n):
    v = list(map(int, input().split()))
    u = v[0] - 1
    for j in v[2:]:
        a[u].append(j-1)

d = [0] * n
f = [0] * n
isDiscovered = [False] * n
time_stamp = 0

def dfs(x):
    global time_stamp
    isDiscovered [x] = True
    time_stamp += 1
    d[x] = time_stamp
    for i in a[x]:
        if not isDiscovered[i]:
            dfs(i)
    time_stamp += 1
    f[x] = time_stamp

for i in range(n):
    if not isDiscovered[i]:
        dfs(i)

for i in range(n):
    print(i+1, d[i], f[i])