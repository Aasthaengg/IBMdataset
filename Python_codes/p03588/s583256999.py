n=int(input())
ans=1
a_max=0
for i in range(n):
    a,b=map(int,input().split())
    if a_max<a:
        ans=a+b
        a_max=a
print(ans)