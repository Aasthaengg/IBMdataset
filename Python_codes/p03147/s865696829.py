n=int(input())
h=list(map(int,input().split()))
count=0
while h!=[0]*n:
    for i in range(n):
        if h[i]!=0:
            start=i
            break
    end=n-1
    for j in range(i+1,n):
        if h[j]==0:
            end=j-1
            break
    for k in range(start,end+1):
        h[k]-=1
    count+=1
print(count)
