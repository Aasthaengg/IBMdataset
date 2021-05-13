n,x = map(int,input().split())
M = list()
ans = 0
for i in range(n):
  m = int(input())
  x-=m
  ans += 1
  M.append(m)
ans += x//min(M)
print(ans)