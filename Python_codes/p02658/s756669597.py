#ABC169-B
n=int(input())
c=list(map(int, input().split()))
ans=1
if 0 in c:
  print(0)
else:
  for i in range(n):
    ans*=c[i]
    if ans>10**18:
      ans=-1
      break
  print(ans)