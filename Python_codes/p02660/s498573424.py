N = int(input())
ans = 0
d = 2
while d*d <= N:
  e = 0
  while N%d == 0:
    e+=1
    N//=d
  i=1
  while i<=e:
    ans+=1
    e-=i
    i+=1
  d+=1

if N>1:
  ans+=1
print(ans)