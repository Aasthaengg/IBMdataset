N=int(input())
B=int(input())
ans=0
X=list(map(int,input().split()))
for i in range(N):
  left=X[i]*2
  right=(B-X[i])*2
  ans+=min(left,right)
print(ans)