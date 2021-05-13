def ip():return int(input())
ans=0
m=10
for i in range(5):
    a=ip()
    if a%10>0:
        ans+=(a//10+1)*10
    else:ans+=a
    if a%10>0:m=min(m,a%10)
print(ans-(10-m))
