n,m = map(int,input().split())
# ab = [list(map(int,input().split())) for i in range(m)]
v = [[] for i in range(n+1)]
# print(v)
for i in range(m):
    a,b = map(int,input().split())
    v[a].append(b)
    v[b].append(a)
while v[1]:
    temp = v[1].pop()
    if n in v[temp]:
        print("POSSIBLE")
        exit()
print("IMPOSSIBLE")