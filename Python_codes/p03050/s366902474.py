def factor(N):
    arr=[]
    for i in range(1,int(N**0.5)+1):
        if(N%i==0):
            arr.append(i)
            if(N//i!=i):
                arr.append(N//i)
    return arr
N=int(input())
arr=factor(N)
ans=0
for x in arr:
    m=N//x-1
    if m<=x:
        continue
    ans+=m
print(ans)