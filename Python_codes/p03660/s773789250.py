n=int(input())
ab=[list(map(int,input().split())) for i in range(n-1)]
data=[[] for i in range(n+1)]
for u in ab:
    a,b=u
    data[a].append(b)
    data[b].append(a)
flag=[0]*(n+1)
s=[1]
g=[n]
flag[1]="B"
flag[n]="W"
while s or g:
    H=[]
    for u in s:
        for v in data[u]:
            if flag[v]==0:
                flag[v]="B"
                H.append(v)
    s=H
    H=[]
    for u in g:
        for v in data[u]:
            if flag[v]==0:
                flag[v]="W"
                H.append(v)
    g=H
Bcount=0
Wcount=0
for i in range(1,n+1):
    if flag[i]=="B":
        Bcount+=1
    elif flag[i]=="W":
        Wcount+=1
if Bcount>Wcount:
    print("Fennec")
else:
    print("Snuke")