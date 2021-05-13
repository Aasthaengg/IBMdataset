n=int(input())
a=list(map(int,input().split()))
ans=3**n
num=1
for i in range(n):
    if a[i]%2==0:
        num*=2
ans-=num
print(ans)