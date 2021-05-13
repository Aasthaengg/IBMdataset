A,B,C,K=map(int,input().split())
if K%2==0:
  ans=A-B
else:
  ans=B-A
if abs(ans)>=1000000000000000000:
  print("Unfair")
else:
  print(ans)