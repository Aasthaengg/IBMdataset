import sys
input=sys.stdin.readline
n=int(input())
button=[False]*(n+1)
button[1]=True
a={}
for i in range(1,n+1):
    ai=int(input())
    a[i]=ai
tmp=1
pushed={}
ans=0
while not button[2]:
    button[tmp]=False
    if tmp in pushed:
        print(-1)
        exit()
    pushed[tmp]=1
    tmp=a[tmp]
    button[tmp]=True
    ans+=1
print(ans)