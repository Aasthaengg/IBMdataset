k,t=map(int,input().split())
a=list(map(int,input().split()))

ans=max(max(a)-1 - (k-max(a)),0)
print(ans)