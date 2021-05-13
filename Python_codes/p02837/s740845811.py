n = int(input())
ls = [[] for _ in range(n)]
di = []
for p in range(n):
    a = int(input())
    ls[p] = [list(map(int,input().split())) for _ in range(a)]
for i in range(2**n):
    new = []
    for j in range(n):
        if (i>>j)&1:
            new.append(j)
    di.append(new)
flag = True
mx = 0
for l in di:
    flag = True
    for k in l:
        for s in ls[k]:
            a,b = s[0],s[1]
            if ((a-1 not in l)and (b == 1)) or ((a-1 in l) and (b == 0)):
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        if len(l) > mx:
            mx = len(l)     
print(mx) 