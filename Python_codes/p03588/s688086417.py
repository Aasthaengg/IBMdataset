N=int(input())
AB=[]
for i in range(N):
    AB.append(list(map(int,input().split())))
a=AB[0][1]
b=0
for i in range(1,N):
    if AB[i][1]<a:
        a=AB[i][1]
        b=i
print(a+AB[b][0])