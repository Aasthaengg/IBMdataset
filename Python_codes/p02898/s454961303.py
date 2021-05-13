N,K=map(int,input().split())
h=[int(x) for x in input().split()]
ans=sum(x>=K for x in h)
print(ans)
