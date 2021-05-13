import sys
input=sys.stdin.readline
n,a,b=map(int,input().split())
x_list=list(map(int,input().split()))
l=b//a
ans=0
for i in range(1,n):
    d=x_list[i]-x_list[i-1]
    if d>l:
        ans+=b
    else:
        ans+=d*a
print(ans)

