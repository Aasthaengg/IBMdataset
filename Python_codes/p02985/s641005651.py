import sys
input = sys.stdin.readline
mod = 10**9+7
rng = 100001
fctr = [1]
finv = [1]
for i in range(1,rng):
    fctr.append(fctr[-1]*i%mod)
for i in range(1,rng):
    finv.append(pow(fctr[i],mod-2,mod))
n,k = map(int,input().split())
ab = [list(map(int, input().split(' '))) for i in range(n-1)]
graph = [[] for i in range(n+1)]
parent = [0 for i in range(n+1)]
cnum = [0 for i in range(n+1)]
root = 1
stack = [root]
ans = 1
for a,b in ab:
    graph[a].append(b)
    graph[b].append(a)
while stack:
    x = stack.pop()
    for y in graph[x]:
        if parent[x] == y:
            continue
        parent[y] = x
        cnum[x] += 1
        stack.append(y)
for x in range(1,n+1):
    if x == 1:
        y = cnum[1]
        if k-y-1<0:
            print(0)
            exit()
        ans = ans*fctr[k]*finv[k-y-1]%mod
        continue
    if cnum[x] == 0:
        continue
    y = cnum[x]
    if k-y-2<0:
        print(0)
        exit()
    ans = ans*fctr[k-2]*finv[k-2-y]%mod
print(ans)