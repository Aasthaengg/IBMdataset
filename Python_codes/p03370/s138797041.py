n,x=map(int,input().split())
a=[int(input()) for _ in range(n)]
y=x-sum(a)
z=y//min(a)
print(n+z)