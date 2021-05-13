N,M = map(int,input().split())
A = list(map(int,input().split()))
lim = sum(A)/(4*M)
ans = 0

for a in A:
  if a>=lim:
    ans+=1
    
if ans>=M:
  print("Yes")
else:
  print("No")