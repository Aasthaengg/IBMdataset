def solve(l):
  a,b,c = 0,0,0
  for i in range(m):
    a += l[i][0]
    b += l[i][1]
    c += l[i][2]
  return abs(a) + abs(b) + abs(c)

n,m = map(int,input().split())
lis = [list(map(int,input().split())) for i in range(n)]
ans = 0

lis.sort(key = lambda x:x[0]+x[1]+x[2])
ans = max(ans,solve(lis))

lis.sort(key = lambda x:x[0]+x[1]-x[2])
ans = max(ans,solve(lis))

lis.sort(key = lambda x:x[0]-x[1]+x[2])
ans = max(ans,solve(lis))

lis.sort(key = lambda x:x[0]-x[1]-x[2])
ans = max(ans,solve(lis))

lis.sort(key = lambda x:-x[0]+x[1]+x[2])
ans = max(ans,solve(lis))

lis.sort(key = lambda x:-x[0]+x[1]-x[2])
ans = max(ans,solve(lis))

lis.sort(key = lambda x:-x[0]-x[1]+x[2])
ans = max(ans,solve(lis))

lis.sort(key = lambda x:-x[0]-x[1]-x[2])
ans = max(ans,solve(lis))

print(ans)