n=int(input())
s=[input() for i in range(n)]
p,m=[],[]
res=0
for i in range(n):
    lr=0
    min_=0
    for c in s[i]:
        if c=='(':
            lr+=1
        else:
            lr-=1
        min_=min(min_,lr)
    if lr>=0:
        p.append([lr,min_])
    else:
        m.append([lr,min_])
    res+=lr
if res!=0:
    print('No')
    exit()
p.sort(key=lambda x:x[1],reverse=True)
m.sort(key=lambda x:(x[0]-x[1]),reverse=True)
cum=0
for x,y in p:
    if cum+y<0:
        print('No')
        exit()
    cum+=x
for x,y in m:
    if cum+y<0:
        print('No')
        exit()
    cum+=x
print('Yes')