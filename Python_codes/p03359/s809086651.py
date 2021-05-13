a,b=map(int,input().split())
m=[0,2,0,1,0,1,0,0,1,0,1,0]
d=[31,30,28]
takahashi=0
for i in range(len(m)):
    for j in range(d[m[i]]):
        if i==j: takahashi+=1
        if a==i+1 and b==j+1: break
    if a==i+1: break
print(takahashi)