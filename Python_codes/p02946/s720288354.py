k,x=map(int,input().split())
ans=list(range(x-k+1,x+k))
ans=map(str,ans)
print(" ".join(ans))