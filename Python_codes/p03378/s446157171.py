N,M,X=map(int,input().split())
A=[int(x) for x in input().split()]
ans=min(sum(x<X for x in A),sum(x>X for x in A))
print(ans)
