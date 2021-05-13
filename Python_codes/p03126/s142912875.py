n,m=map(int,input().split())
ans={i for i in range(1,m+1)}
for i in range(n):
    a=[int(i) for i in input().split()]
    a=a[1:]
    ans=ans&set(a)
print(len(list(ans)))