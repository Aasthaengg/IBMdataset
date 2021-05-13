n, m, q = map(int,input().split())
ways = [[0 for i in range(n+2)] for j in range(n+2)]
for i in range(m):
    l,r = map(int,input().split())
    ways[l][r] += 1

sgways = [[0 for i in range(n+2)] for j in range(n+2)]
for j in range(1,n+1):
    for i in range(j):
        sgways[j-i][j] = sgways[j-i+1][j] +ways[j-i][j]

ans = [[0 for i in range(n+1)] for j in range(n+1)]
for i in range(1,n+1):
    for j in range(i,n+1):
        ans[i][j] = ans[i][j-1]+sgways[i][j]
for i in range(q):
    pi,qi = map(int,input().split())
    print(ans[pi][qi])
