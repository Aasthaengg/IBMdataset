n = int(input())
d, x = map(int, input().split())
ans = x
for i in range(n):
  a = int(input())
  res = (d-1)//a
  ans += res+1
  
print(ans)  