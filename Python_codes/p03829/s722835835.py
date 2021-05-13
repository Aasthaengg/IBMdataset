N,a,b=map(int,input().split())
X=list(map(int,input().split()))
cnt=0
for i in range(N-1):
  d=X[i+1]-X[i]
  if d*a>b:
    cnt+=b
  else:
    cnt+=d*a
print(cnt)