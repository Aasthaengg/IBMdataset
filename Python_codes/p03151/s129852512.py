import sys
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ab=[]
ans=0
tmp=0
if sum(b)>sum(a):
    print(-1)
    sys.exit()
for i in range(n):
    ab.append(a[i]-b[i])
    if a[i]-b[i]<0:
        ans+=1
        tmp+=a[i]-b[i]
ab.sort()
if ans ==0:
    print(ans)
while tmp<0:
    tmp+=ab.pop()
    ans+=1
    if tmp>=0:
        print(ans)
        sys.exit