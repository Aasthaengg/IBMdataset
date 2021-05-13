N,M,X=map(int,input().split())
A=list(map(int,input().split()))
l=[(1 if i in A else 0) for i in range(N+1)]
print(min(sum(l[:X+1]),sum(l[X:])))