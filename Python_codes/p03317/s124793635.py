n,k=map(int,input().split())
a=[int(x) for x in input().split()]
ans=1
n-=k
k-=1
ans+=(n+k-1)//k
print(ans)
