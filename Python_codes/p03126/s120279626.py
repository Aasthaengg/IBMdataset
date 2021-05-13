n,m=map(int,input().split())
li=[list(map(int, input().split()))[1:] for _ in range(n)]
res=[0]*m
for i in range(n):
    for j in range(len(li[i])):
        res[li[i][j]-1]+=1
print(res.count(n))