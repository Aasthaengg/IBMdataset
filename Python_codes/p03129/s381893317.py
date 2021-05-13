n,k=map(int,input().split())
if (n%2==0 and k <=n//2) or (n%2==1 and k <= (n+1)//2):
  print("YES")
else:
  print("NO")