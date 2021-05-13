import itertools
 
n,m,r_ = map(int, input().split( ))
 
r = list(map(int, input().split( )))
for i in range(r_):
  	r[i] -= 1
d = [[10**10 for _ in range(n)] for i in range(n)]
 
for i in range(m):
    ai,bi,ci = map(int, input().split( ))
    ai-=1
    bi-=1
    d[ai][bi] = d[bi][ai] = ci

for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][k]+d[k][j],d[i][j])
ans= 100000000000000
for l in itertools.permutations(r,r_):
    tmp = 0
    for i in range(r_-1):
        tmp += d[l[i]][l[i+1]]
    ans = min(ans, tmp)
 
print(ans)