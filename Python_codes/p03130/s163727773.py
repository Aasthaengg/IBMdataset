G = [list(map(int,input().split())) for i in range(3)]
deg = [0]*4
for x in G:
    deg[x[0]-1] += 1
    deg[x[1]-1] += 1
odd = 0
for x in deg:
    if x%2 == 1:
        odd += 1
if odd == 0 or odd ==2:
    print("YES")
else:
    print("NO")