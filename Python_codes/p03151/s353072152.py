n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
lack=0
num=[]
count=0
c=0
if sum(a)<sum(b):
    print(-1)
    
else:
    for i in range(n):
        if b[i]>a[i]:
            lack+=b[i]-a[i]
            count+=1
        if b[i]<a[i]:
            num.append(a[i]-b[i])
    if count!=0:
       num.sort(reverse=True)
       for i in range(len(num)):
           c+=num[i]
           count+=1
           if c>=lack:
            break
    print(count)