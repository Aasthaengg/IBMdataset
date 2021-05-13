n = int(input())

def wa(n):
  ret = 0
  while n > 0:
    ret += n%10
    n //= 10
  return ret

ans = 10**10
for a in range(1,n):
  b = n-a
  ans = min(ans,wa(a)+wa(b))  
  
print(ans)  