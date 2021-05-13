K,X=map(int,input().split())
a=X-(K-1)
b=X+(K)
l=list(range(a,b))

ans=""

for L in l:
  s=str('{} '.format(L))
  ans+=s

print(ans)