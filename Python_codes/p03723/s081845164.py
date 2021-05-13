def check(A,B,C):
  if A==0 or B==0 or C==0:
    return False
  if A%2!=0 or B%2!=0 or C%2!=0:
    return False
  return True

A,B,C=map(int,input().split())
ans=0
if A%2==B%2==C%2==0 and A==B==C:
  print(-1)
  exit()
while check(A,B,C)==True:
  a=B//2+C//2
  b=A//2+C//2
  c=A//2+B//2
  A,B,C=a,b,c
  ans+=1
  if 10**9<ans:
    ans=-1
    break
print(ans)
