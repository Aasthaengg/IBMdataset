def ip():return int(input())

ans=0
m=99
for _ in range(ip()):
    p=ip()
    ans+=p
    m=max(m,p)
print(ans-m//2)