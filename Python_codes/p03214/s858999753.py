n=int(input())
a=list(map(int,input().split()))

ave=sum(a)/n
d=1001001001001
ans=0

for i in range(n):
    if d > abs(a[i]-ave):
        d=min(d,abs(a[i]-ave))
        ans=i
    
print(ans)