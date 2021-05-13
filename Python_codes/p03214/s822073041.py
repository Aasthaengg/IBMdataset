n=int(input())
a=list(map(int,input().split()))

tmp=sum(a)/n
cnt=100000 -tmp
ans=0
for i in range(len(a)):
    if cnt>abs(tmp-a[i]):
        ans=i
        cnt=abs(tmp-a[i])

print(ans)