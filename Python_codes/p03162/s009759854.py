n=int(input())
arr=[]
res=[]
for i in range(n):
    inp = list(map(int,input().split()))
    arr.append(inp)
res.append(arr[0][0])
res.append(arr[0][1])
res.append(arr[0][2])
for i in range(1,len(arr)):
    x=[-1,-1,-1]
    x[0]=max(res[1],res[2])+arr[i][0]
    x[1]=max(res[0],res[2])+arr[i][1]
    x[2]=max(res[0],res[1])+arr[i][2]
    res=x
print (max(res))