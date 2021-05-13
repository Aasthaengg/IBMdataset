n,m = map(int,input().split())
pre = [[] for _ in range(n)]
num=[]
for i in range(m):
    p,y = map(int,input().split())
    pre[p-1].append([i,y])
for i in range(n):
    pre[i].sort(key=lambda x:x[1])
    for j in range(len(pre[i])):
        num.append([pre[i][j][0],('0'*5+str(i+1))[-6:]+('0'*5+str(j+1))[-6:]])
num.sort(key=lambda x:x[0])
for k in num:
    print(k[1])