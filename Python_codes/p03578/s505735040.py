n=int(input())
d=list(map(int,input().split()))
m=int(input())
t=list(map(int,input().split()))
dd=dict()
td=dict()
for i in d:
    if i in dd:
        dd[i]+=1
    else:
        dd[i]=1
for i in t:
    if i in td:
        td[i]+=1
    else:
        td[i]=1
for i,j in td.items():
    if i not in dd:
        print('NO')
        exit()
    elif dd[i]<j:
        print('NO')
        exit()
print('YES')