n,m=map(int,input().split())
pre=[[] for _ in range(n)]
for _ in range(m):
    p,y=map(int,input().split())
    pre[p-1].append([y,_,p])
for p in range(n):
    pre[p].sort(key=lambda x:x[0])
    for i in range(len(pre[p])):
        pre[p][i].append(i)
lis=[]
for i in pre:
    for j in i:
        lis.append(j)
lis.sort(key=lambda x:x[1])
for i in lis: print("{:06}{:06}".format(i[2],i[3]+1))