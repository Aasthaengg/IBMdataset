n = int(input())
a = [0 for _ in range(n)]
x = [[] for i in range(n)]
y = [[] for i in range(n)]
for i in range(n):
    a[i] = int(input())
    for j in range(a[i]):
        s,t = map(int,input().split())
        x[i].append(s)
        y[i].append(t)
ans = 0
for i in range(2**n):
    karishoujiki = []
    shoujiki = []
    usotuki = []
    for j in range(n):
        if (i>>j)&1:
            karishoujiki.append(j)
            for k in range(a[j]):
                if y[j][k] == 1:
                    shoujiki.append(x[j][k]-1)
                else:
                    usotuki.append(x[j][k]-1)
    flag = 1
    shoujikiflag = [0 for _ in range(n)]
    karishoujikiflag = [0 for _ in range(n)]
    usotukiflag = [0 for _ in range(n)]
    for i in range(len(shoujiki)):
        shoujikiflag[shoujiki[i]] = 1
    for i in range(len(karishoujiki)):
        karishoujikiflag[karishoujiki[i]] = 1
    for i in range(len(usotuki)):
        usotukiflag[usotuki[i]] = 1
    
    for i in range(n):
        if shoujikiflag[i] and not karishoujikiflag[i]:
            flag = 0
        if usotukiflag[i] and karishoujikiflag[i]:
            flag = 0
    
    if flag:
        ans = max(ans,len(karishoujiki))

print(ans)