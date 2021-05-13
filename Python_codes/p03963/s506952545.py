n, k = map(int, input().split())
ans = k
n -= 1
while n != 0:
  ans *= (k-1)
  n -= 1
  
print(ans)