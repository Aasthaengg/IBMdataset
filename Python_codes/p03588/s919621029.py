n = int(input())
ans = 0
c = 0
for _ in range(n):
  a, b = map(int, input().split())
  if a > c:
    ans = a+b
    c = a
    
print(ans)