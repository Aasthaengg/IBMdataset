n,k=map(int,input().split())
x=list(map(int,input().split()))
x.sort()
ans=[]
for i in range(0,n-k+1):
  l=x[i]
  r=x[i+k-1]
  ans.append(min(abs(l)+abs(l-r),abs(r)+abs(l-r)))
print(min(ans))