n=int(input())
dx = n
ans = 1
while dx%360>0:
  ans+=1
  dx += n
print(ans)