n,m=map(int,input().split())
a=list(map(int,input().split()))
arr=[]

for i in range(m):
    b,c=map(int,input().split())
    arr.append((b,c))

a=sorted(a)
arr=sorted(arr,key=lambda x:-x[1])

flag=0
left=0
for tup in arr:
    for i in range(left,min(left+tup[0],n)):
        if tup[1]>a[i]:
            a[i]=tup[1]
        else:
            flag=-1
            break
        if i==n-1:
            flag=-1
            break
    left+=tup[0]
    if flag==-1:
        break

print(sum(a))