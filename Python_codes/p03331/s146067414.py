n = int(input())
def digsum(x):
  ret = 0
  while x > 0:
    ret += x % 10
    x //= 10
  return ret
ans = 10**5
for i in range(1, (n+1)//2+1):
  ans = min(ans, digsum(i) + digsum(n-i))
print(ans)