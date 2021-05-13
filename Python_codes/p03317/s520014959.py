n,k=map(int,input().split())
a=[int(x) for x in input().split()]
ans=(n-1)//(k-1)
if (n-1)%(k-1)!=0:
  ans+=1
print(ans)
