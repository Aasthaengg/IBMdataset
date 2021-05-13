n=int(input())
a=list(map(int,input().split()))
ans = 0
for i in range(n-1):
  s = a[i+1] -a[i] 
  if s < 0:
      ans = ans - s
      a[i+1]=a[i]
print(ans)