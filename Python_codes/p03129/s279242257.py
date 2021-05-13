N,K=map(int,input().split())
if N%2==1:
  s=N//2+1
else:
  s=N//2
if K<=s:
  print("YES")
else:
  print("NO")