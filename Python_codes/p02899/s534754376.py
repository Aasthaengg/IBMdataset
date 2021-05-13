n=int(input())
a=[0]+list(map(int,input().split()))

ans=[0]*n
for i in range(1,n+1):
  ans[a[i]-1]=i

ans=" ".join(map(str,ans))
print(ans)