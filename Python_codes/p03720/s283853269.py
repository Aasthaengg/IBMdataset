n,m = map(int,input().split())
x = [list(map(int,input().split())) for i in range(m)]
y = []
z = []

for k in range(m):
    y = y + x[k]

for l in range(1,n+1):
    z = z + [y.count(l)]
    
for p in z:
    print(p)