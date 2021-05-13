N,Y = map(int,input().split())

check = False
for i in range(N+1):
  for j in range(N+1):
    k = (Y - 10000 * i - 5000 * j) / 1000
    if k != int(k) or k < 0 or k != N - i - j:
      continue
    else:
      check = True
      ans = [i,j,int(k)]
      
if not check:
  ans = [-1,-1,-1]
print(*ans)