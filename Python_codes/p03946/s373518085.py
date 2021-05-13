n,t=map(int,input().split())
a=list(map(int,input().split()))
list1=[0]*n
list1[0]=a[0]
list2=[0]*n
list2[n-1]=a[n-1]
for i in range(1,n):
    list1[i]=min(list1[i-1],a[i])
for i in range(n-2,-1,-1):
    list2[i]=max(list2[i+1],a[i])
lst=[]
for i in range(n):
    lst.append([list2[i]-list1[i],list1[i]])
count=1
lst.sort(reverse=True)
for i in range(1,n):
    if lst[i][0]==lst[i-1][0]:
        if lst[i][1]!=lst[i-1][1]:
            count+=1
    else:
        break
print(count)