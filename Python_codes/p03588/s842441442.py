n=int(input())
t=0
ans=0
for i in range(n):
    a,b=map(int,input().split())
    if t<a:
        ans=a+b
        t=a
print(ans)