n,k=map(int,input().split())
k-=1
a=list(map(int, input().split()))
i=n-1
print(-(-i//k)-(-(n-i-1)//k))#pythonで切り上げの書き方