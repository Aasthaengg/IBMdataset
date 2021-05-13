n,x=map(int,input().split())

a=list(map(int,input().split()))

a.sort()

count=0
 
if x<a[0]:
    print(0)
    exit()


for i in range(n):
    if x>=a[i]:
        x-=a[i]
        count+=1
    else:
        print(count)
        exit()

if x>0:
    print(count-1)
else:
    print(count)