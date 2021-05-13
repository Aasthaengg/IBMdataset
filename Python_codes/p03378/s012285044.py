n,m,x=map(int,input().split())
a=sorted(list(map(int,input().split())))
plus=0
minus=0
for i in a:
    if i<x:
        minus+=1
    else:
        plus+=1
print(min(minus,plus))