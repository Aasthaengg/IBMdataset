import itertools

n=int(input())

lst=[[] for i in range(n)] 

for i in range(n):
  a=int(input())
  for j in range(a):
    x,y=map(int,input().split())
    lst[i].append([x-1,y])

ans=0


for xxx in itertools.product(range(2),repeat=n):
    table=[[] for i in range(n)]
    for j in range(n):
        if xxx[j]==1:
            for k in lst[j]:
                table[k[0]].append(k[1])
    
    flag=True

    for j in range(n):
        if xxx[j]==1:
            if table[j].count(0)!=0:
                flag=False
        
        else:
            if table[j].count(1)!=0:
                flag=False
    

    if not flag:
        continue
    

    ans=max(ans,xxx.count(1))



print(ans)