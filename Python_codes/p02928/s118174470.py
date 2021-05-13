n,k=map(int,input().split())
mod=10**9+7
a=list(map(int,input().split()))
tcount=0
hidaricount=[]
allcount=[]

for i in range(n):
    count=0
    for j in range(n):
        #print(a[i],a[j],"all")
        if a[i]<a[j]:
            count+=1
    allcount.append(count)


for i in range(n):
    count=0
    for j in range(i+1,n):
        #print(a[i],a[j])
        if a[i]<a[j]:
            count+=1
    hidaricount.append(count)  
#print(allcount)
#print(hidaricount)  
#print(sum(allcount),sum(hidaricount))
alls=sum(allcount)
hidari=alls-sum(hidaricount)
#print(alls,hidari)
print((hidari*k + alls*k*(k-1)//2 )%mod)
