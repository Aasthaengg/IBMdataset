a,b,c,k=map(int,input().split())
ans=(-1)**k*(a-b)
print(['Unfair',ans][int(abs(ans)<10**18)])