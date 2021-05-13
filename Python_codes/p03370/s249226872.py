n,x=map(int,input().split())
li=[int(input()) for i in range(n)]
ans=n
x-=sum(li)
print(n+x//min(li))
