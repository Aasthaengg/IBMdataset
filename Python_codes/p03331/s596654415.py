n=int(input())
ans=1e10
for i in range(1,n//2+1):
  ans=min(ans,sum(map(int,list(str(i))))+sum(map(int,list(str(n-i)))))
print(ans)