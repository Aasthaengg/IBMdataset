n=int(input())
a=list(map(int,input().split()))
flag=True
s=False
e=0
c=1
for i in range(1,n):
    if a[i]==a[i-1]:
        continue
    if a[i]>a[i-1]:
        flag=True
        e=i
        break
    elif a[i]<a[i-1]:
        flag=False
        e=i
        break
if e==n:
    print(1)
    exit()

for i in range(e+1,n):
    if a[i]==a[i-1]:
        continue
    if s==True:
        if a[i]>a[i-1]:
            s=False
            flag=True
        else:
            s=False
            flag=False
    elif a[i]>a[i-1] and flag==False:
        c+=1
        s=True
    elif a[i]<a[i-1] and flag==True:
        c+=1
        s=True
print(c)