from sys import setrecursionlimit as SRL, stdin

SRL(10 ** 7)
rd = stdin.readline
rrd = lambda: map(int, rd().strip().split())

q = [[]]
l = [0] * 1005
d = [0] * 1005
hv = [0] * 1005

def dfs(x,y):
    hv[x] = 1
    for i in range(l[x],n-1):

        if q[x][i] == y:
            l[x] = i+1
            hv[x] = 0

            d[q[x][i]] += 1
            d[x] += 1
            d[x] = max(d[x],d[q[x][i]])
            d[q[x][i]] = max(d[x], d[q[x][i]])

            return
        if hv[q[x][i]]:
            print(-1)
            exit(0)
        dfs(q[x][i],x)
        d[x] = max(d[q[x][i]],d[x])


    hv[x] = 0
    l[x] = n

n = int(input())
for i in range(n):
    a = list(rrd())
    q.append(a)

for i in range(1,n+1):
    dfs(i,0)

print(max(d))
