n=int(input())
alist=list(map(int,input().split()))

alist.sort()
gomi=0
for i in range(1,n):
    if alist[i]==alist[i-1]:
        gomi+=1
if gomi%2==0:
    ans=n-gomi
else:ans=n-gomi-1
print(ans)
