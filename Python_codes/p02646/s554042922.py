#n=int(input())
a, v=map(int,input().split())
b,w=map(int,input().split())
t=int(input())
#al=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
ans="NO"
if a<b:
    a+=v*t;b+=w*t
    if a>=b:
        ans="YES"
else:
    a-=v*t;b-=w*t
    if a<=b:
        ans="YES"

print(ans)