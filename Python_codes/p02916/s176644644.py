n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))

anker=-10
ans=0
for i in range(1,n+1):
    cuisine=a.index(i)
    if cuisine-anker==1:
        ans += c[i-2]
    anker = cuisine
ans += sum(b)
print(ans)
