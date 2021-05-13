N = int(input())
ls = [-1]
for i in range(N):
  ls += [int(input())]

ans = 0
p = 0
for i in range(1,N+1):
  if ls[i-1]+1<ls[i]:
    print(-1)
    break
  if ls[i-1]+1==ls[i]:
    if i==N:
      ans += (ls[i])
    p = ls[i]
    continue
  else:
    if i==N:
      ans += ls[i]
    ans += p
    p = ls[i]
else:
  print(ans)