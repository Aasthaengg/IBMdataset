n,x=map(int,input().split())
a=[int(input()) for _ in range(n)]

cnt=n
x-=sum(a)
cnt+=x//min(a)

print(cnt)
