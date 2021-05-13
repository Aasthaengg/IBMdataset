mod=10**9+7
a,b=map(int,input().split())

if abs(a-b)>=2:
    print(0)
    exit()

ans=1
for i in range(2,a+1):
    ans*=i
    ans%=mod

for i in range(2,b+1):
    ans*=i
    ans%=mod

if a==b:
    ans*=2
    ans%=mod

print(ans)