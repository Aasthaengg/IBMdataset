n,m = map(int,input().split())
d = [0 for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    d[a] = 1-d[a]
    d[b] = 1-d[b]

if sum(d) == 0:
    print("YES")
else:
    print("NO")