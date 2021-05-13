n=int(input())
a=list(map(int,input().split()))
m=int(input())
alls=sum(a)
for _ in range(m):
    p,x=map(int,input().split())
    print(alls + x - a[p-1])