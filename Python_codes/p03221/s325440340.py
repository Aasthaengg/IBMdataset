n,m= map(int, input().split())
x= [list(map(int, input().split())) for i in range(m)]

for i in range(m):
    x[i].append(i)

# 県ごとに格納
v=[[] for i in range(n+1)]
# 答えを格納
ans=[0 for i in range(m)]

for i in range(m):
    v[x[i][0]].append(x[i])

for i in range(n+1):
    v[i].sort()
#print(v)
for i in range(n+1):
    for j in range(len(v[i])):
        # 上６桁
        l=str(0)*(6-len(str(i)))+str(i)
        ans[v[i][j][2]]=l+str(0)*(6-len(str(j+1)))+str(j+1)

for i in range(m):
    print(ans[i])