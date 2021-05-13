#n=int(input())
a,b,c=map(int,input().split())
#al=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

mx=max(a,b,c)
dif=3*mx-(a+b+c)
if dif%2==0:
    ans=dif//2
else:
    ans=dif//2+2

print(ans)