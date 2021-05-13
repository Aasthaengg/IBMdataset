N = int(input())
L=[[0 for i in range(10)] for j in range(10)]
for i in range(1,N+1):
    a=i%10
    if i<10:
        b=i
    c=i
    while c>=10:
        b=c//10
        c=b
    L[b][a]+=1
num=0
for i in range(10):
    for u in range(10):
        if L[i][u]!=0:
            num+=L[i][u]*L[u][i]
print(num)