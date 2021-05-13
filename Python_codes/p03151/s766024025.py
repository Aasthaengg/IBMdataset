n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

dif=sum(a)-sum(b)
if dif<0:
    print(-1)
    
elif dif==0:
    cnt=0
    for i in range(n):
        if a[i]!=b[i]:
            cnt+=1
    print(cnt)
    
else:
    difference=[]
    count_0=0
    for i in range(n):
        if a[i]-b[i]>0:
            difference.append(a[i]-b[i])
        elif a[i]==b[i]:
            count_0+=1
    difference=sorted(difference)
    
    cnt=0
    keep=0
    for i in range(len(difference)):
        if cnt+difference[i]<=dif:
            cnt+=difference[i]
            keep+=1
        else:
            break
    print(n-count_0-keep)