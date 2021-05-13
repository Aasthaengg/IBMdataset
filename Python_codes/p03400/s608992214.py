n = int(input())
d, x = map(int, input().split())

ans = x
for i in range(n):
  a = int(input())
  i = 1
  while i <= d:
    ans += 1
    i += a
    
print(ans)