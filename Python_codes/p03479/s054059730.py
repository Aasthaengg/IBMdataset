a,b = map(int,input().split())
ans = 0
for i in range(10**18+1):
  if a*(2**i) <= b:
    ans += 1
  else:
    break
print(ans)
