k,x=map(int,input().split())
li=[]
for i in range(k-1):
    li.append(x-k+1+i)
li.append(x)
for i in range(k-1):
    li.append(x+1+i)
print(*li)
