n = int(input())
d,x = map(int,input().split())
ans = 0
for i in range(n):
  a = int(input())
  j = 0
  while a*j + 1 <= d:
    ans += 1
    j += 1
  
print(ans+x)
