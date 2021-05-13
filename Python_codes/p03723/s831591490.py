a,b,c = map(int,input().split())
for i in range(600):
  if a&1 or b&1 or c&1:
    break
  a,b,c = a//2, b//2, c//2
  a, b, c = b + c, a + c, a + b
ans = i if i < 500 else -1
print(ans)