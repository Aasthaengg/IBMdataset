a,b,k = map( int,input().split() )

i = min(a,b)
ans = 0
while 1:
  if not(a % i)  and not(b % i):
    ans += 1
  if ans == k:
    break
  i -= 1

print(i)
