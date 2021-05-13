k,x=map(int,input().split())
n=x-k+1
m=x+k
ans=[i for i in range(n,m)]
print(*ans)