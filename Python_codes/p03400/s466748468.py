n=int(input())
d,x=map(int,input().split())
ans=x
for i in range(n):
    a=int(input())
    c=int((d-1)/a)+1
    ans+=c
print(ans)