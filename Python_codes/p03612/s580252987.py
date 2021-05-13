n=int(input())
alis=list(map(lambda x:int(x)-1,input().split()))
counter=0
for i in range(n):
    if i!=n-1:
        if i==alis[i]:
            alis[i],alis[i+1]=alis[i+1],alis[i]
            counter+=1
    else:
        if i==alis[i]:
            alis[i],alis[i-1]=alis[i-1],alis[i]
            counter+=1
print(counter)