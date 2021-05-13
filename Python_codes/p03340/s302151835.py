# ABC098 D - Xor Sum 2
n=int(input())
a=list(map(int,input().split()))

l=0
r=1
tmp=a[0]
ans=0

while l<n:
    if r==n:
        ans+=(r-l)
        l+=1
        continue
    if tmp+a[r]==tmp^a[r]:
        tmp=tmp+a[r]
        r+=1
    else:
        ans+=(r-l)
        tmp=tmp-a[l]
        l+=1      

print(ans)
