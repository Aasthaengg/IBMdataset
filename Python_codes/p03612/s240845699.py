n=int(input())
p=list(map(int,input().split()))

bl=[True]*n
for i in range(n):
    if (i+1)==p[i]:
        bl[i]=False

count=0
for i in range(n-1):
    if bl[i] is False:
        bl[i]=True
        bl[i+1]=True
        count+=1

if bl[n-1] is False:
    count+=1

print(count)