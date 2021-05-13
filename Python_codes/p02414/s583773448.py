n,m,l = tuple(int(x) for x in input().split())
R = []
A = [[int(a) for a in input().split()] for i in range(n)]
B = [[] for j in range(l)]

for j in range(m):
    i = input().split()
    [B[k].append(int(i[k])) for k in range(l)]
    
for a in A:
    rs = []
    for j in range(l):
        rs.append(sum([a[r]*B[j][r] for r in range(m)]))
    R.append(rs)
    
for r in R:
    print(" ".join(map(str,r)))
