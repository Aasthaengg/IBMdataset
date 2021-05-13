n=int(input())
li=[]
cnt=0
for i in range(n):
    li.append(input())

li.sort()
last=li[0]

for i in range(1,n):
    if last==li[i]:
        li[i]=0
    
    else:
        last=li[i]

print(n-li.count(0))
