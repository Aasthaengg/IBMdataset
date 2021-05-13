n=int(input())
l=list(map(int,input().split()))
m=int(input())
for i in range(m):
    x,y=map(int,input().split())
    z=l[x-1]
    l[x-1]=y
    print(sum(l))
    l[x-1]=z
