A,B,T = map(int,input().split())

ans = 0

while T>0:
  ans += B
  T -= A
  
if T == 0:
  print(ans)
else:
  print(ans-B)