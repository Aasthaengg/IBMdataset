N=int(input())
A=list(map(int,input().split()))
x=sum([A[i]*(-1)**i for i in range(N)])
res=[x]
for i in range(N-1):
    x=A[i]*2-x
    res.append(x)
print(*res)