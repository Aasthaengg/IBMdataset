N=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

asum=sum(a)
bsum=sum(b)
if bsum<asum:
    print("No")
    exit()

ab=0
ba=0

for i in range(N):
    if a[i]<b[i]:
        ab+=(b[i]-a[i])//2
    else:
        ba+=a[i]-b[i]

if ab>=ba:
    print("Yes")
else:
    print("No")