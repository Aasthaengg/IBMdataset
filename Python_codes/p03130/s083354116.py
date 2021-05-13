# 2019/11/27

edge=[[] for _ in range(4)]
for _ in range(3):
    a,b=map(int,input().split())
    a,b=a-1,b-1
    edge[a].append(b)
    edge[b].append(a)

odd=0
for c in edge:
    if len(c)%2:odd+=1
print('YES' if odd==2 else 'NO')
