n=int(input())
if n>2 and n%2!=0:
    n-=1
cnt=1
ans=n
for i in range(1,n+1)[::-2]:
    j=i
    tmp=0
    while j>0 and j%2==0:
        tmp+=1
        j=j//2
    if tmp > cnt:
        cnt=tmp
        ans=i
print(ans)