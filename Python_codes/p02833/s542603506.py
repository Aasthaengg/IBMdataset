n=int(input())
ans=0
if n%2==0:
    for i in range(1,30):
        m=n//((5**i)*2)
        ans+=m
print(ans)