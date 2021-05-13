n=int(input())
#a,b=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
s=list(input())

x=0
mx=0

for si in s:
    if si=='I':
        x+=1
    else:
        x-=1
    mx=max(x,mx)
print(mx)