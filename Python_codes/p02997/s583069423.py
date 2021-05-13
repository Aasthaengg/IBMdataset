n,k = map(int, input().split())
m = (n-1)*(n-2)//2
if k > m:
    print(-1)
    exit()
r = m-k

edge = [[] for i in range(n)]
edge[0] = list(range(1, n))
for i in range(1, n):
    for j in range(i+1, n):
        if r == 0:
            break
        edge[i].append(j)
        r -= 1

m = sum(len(i) for i in edge)
print(m)
for i in range(n):
    for j in edge[i]:
        print(i+1, j+1)