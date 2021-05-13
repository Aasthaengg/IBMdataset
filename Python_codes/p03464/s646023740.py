k=int(input())
a=list(map(int,input().split()))
m=2
M=2
for i in range(k-1,-1,-1):
    x=a[i]
    r=M//x
    l=(m-1)//x
    if r-l<1:
        print(-1)
        exit()
    m=(m+x-1)//x*x
    M=M//x*x+x-1
print(m,M)
