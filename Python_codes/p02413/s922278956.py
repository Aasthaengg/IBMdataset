ls = []
ls2=[]
r,c = map(int,input().split())
for i in range(0, r):
    ls.append(list(map(int,input().split())))

for j in range(0, r):
    ls[j].append(sum(ls[j]))

for j in range(0, c+1):
    num = 0
    for k in range(0, r):
        num += ls[k][j]
    ls2.append(num)
ls.append(ls2)
for z in range(0, r+1):
    print(*ls[z])