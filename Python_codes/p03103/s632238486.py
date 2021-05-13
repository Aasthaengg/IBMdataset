n,m=map(int,input().split())
num=[]
for i in range(n):
    a,b=map(int,input().split())
    num.append([a,b])
str1= lambda val: val[0]
num.sort(key=str1)
numa=0
numb=0
for i in range(n):
    numa+=(num[i][1])*(num[i][0])
    numb+=num[i][1]
    if numb>=m:
        numa-=(numb-m)*num[i][0]
        break
print(numa)
