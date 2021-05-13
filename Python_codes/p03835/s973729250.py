K,S = map(int,input().split())
ans = 0
if 3*K < S:
  pass
else:
  for x in range(K+1):
    for y in range(K+1):
      z = S-x-y
      if 0 <= z <= K:
        ans += 1

print(ans)