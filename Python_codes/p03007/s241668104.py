N,*A=map(int, open(0).read().split())
A.sort()
m,M=A[0],A[-1]
B=A[1:-1]
ans=[]
for b in B:
    if b>=0:
        ans.append((m,b))
        m-=b
    else:
        ans.append((M,b))
        M-=b
ans.append((M,m))
print(M-m)
for x,y in ans:
    print(x,y)