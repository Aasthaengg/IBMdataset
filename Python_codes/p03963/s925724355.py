a, b = list(map(int, input().split()))
 
ans = b
for i in range(a - 1):
  ans *= b - 1
 
print(ans)