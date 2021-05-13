a=list(map(int, input().split()))
xy=[map(int, input().split()) for l in range(a[0])]
x, y=[list(i) for i in zip(*xy)]
set=[[0 for j in range(2)] for i in range(a[0])]
num=0
for ele in x:
    set[num][0]=x[num]
    set[num][1]=y[num]
    num+=1
set.sort()
num=0
while a[1]>0:
    a[1]=a[1]-set[num][1]
    num+=1
print(set[num-1][0])