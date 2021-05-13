K, A, B = map(int, input().split())
ans = 0
if B>A+1:
  if K>=A+1:
    ans += B
    K -= A+1
    k = K//2
    ans += (B-A)*k
    ans += K%2
  else:
    ans = K+1
    
  
else:
  ans = K+1

print(ans)    