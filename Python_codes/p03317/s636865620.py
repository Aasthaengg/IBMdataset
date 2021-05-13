n,k=map(int,input().split())
cnt=1
n-=k
cnt+=(n+k-2)//(k-1)
print(cnt)