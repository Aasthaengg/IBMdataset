def digitsum(n):
  return sum(list(map(int,list(str(n)))))
N,a,b=map(int,input().split())
ans=0
for i in range(1,N+1):
  if a<=digitsum(i) and b>=digitsum(i):
    ans+=i
print(ans)