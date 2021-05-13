a,b,c,k = map(int,input().split())

if k < a:
  ans = k
if a <= k <= a+b:
  ans = a
if a+b < k < a+b+c:
  ans = a-(k-a-b)
if a+b+c <= k:
  ans = a-c

print(ans)