N=int(input())

if N == 1:
  print(0)
  exit()

ans = 0
i = 1
while True:
  m = N//i-1
  q,r = divmod(N,m)
  if q == r:
    ans += m
  if m<N**.5:
    break
  i += 1
  
print(ans)