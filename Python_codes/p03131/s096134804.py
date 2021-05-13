K,A,B = map(int,input().split())

if K < A+1 or B <= A+2:
  print(K+1)
  exit(0)
  
K -= A - 1
ans = A
p,q = divmod(K,2)
ans += (B-A) * p + q
print(ans)
