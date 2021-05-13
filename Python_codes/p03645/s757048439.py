n,m = map(int,input().split())
dum = [[] for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    dum[a-1].append(b-1)
for i in dum[0]:
    if dum[i].count(n-1) >= 1:
        print("POSSIBLE")
        exit()
print("IMPOSSIBLE")