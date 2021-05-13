a,b=map(int,input().split())
lists=[list("#"*100) for i in range(50)]
lists+=[list("." *100) for i in range(50)]

counter1=0
for i in range(49):
    for j in range(i,95,3):
        if counter1==a-1:
            break
           
        else:
            lists[i][j]="."
            counter1+=1
counter2=0
for i in range(51,100):
    for j in range(i-50,95,3):
        if counter2==b-1:
            break
        else:
            lists[i][j]="#"
            counter2+=1
print(100,100)
for i in range(100):
    a="".join(lists[i])
    print(a)
