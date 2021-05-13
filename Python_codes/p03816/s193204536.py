n=int(input())
a=list(map(int,input().split()))
a.sort()
k=1
lst=[]
for i in range(1,n):
    if a[i]==a[i-1]:
        k+=1
    else:
        lst.append(k)
        k=1
lst.append(k)
m=len(lst)
count=0
for i in range(m):
    if lst[i]%2==0:
        lst[i]=2
        count+=1
    else:
        lst[i]=1
if count%2==0:
    print(m)
else:
    print(m-1)