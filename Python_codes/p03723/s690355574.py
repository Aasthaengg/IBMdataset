a,b,c = map(int,input().split())
ans = 0
for i in range(10000001):
  if a%2 == 1 or b%2 == 1 or c%2 == 1:
    break
  if i == 1000000:
    print(-1)
    exit()
  m = a
  n = b
  l = c
  a = (b+c)//2 
  b = (c+m)//2 
  c = (m+n)//2
  ans += 1
print(ans)