n=int(input())
a=list(map(int, input().split()))
d=sum(a)
ans=d
for i in range(n):
  d=d-2*a[i]
  if abs(d)<ans:
    ans=abs(d)
print(ans)