a,b,c=map(int,input().split())
d=list(map(int,input().split()))
e=[]
total2=0
for i in range(a):
    e.append(list(map(int,input().split())))
for i in range(a):
    total=0
    for j in range(b):
        total+=d[j]*e[i][j]
    if total+c>0:
        total2+=1
print(total2)