N,M = map(int, input().split())
ans = 0
while not (N == 0 and M == 0):
 for i in range(1, N+1):
  for j in range(i+1, N+1):
   k = M - i - j
   if ( k > N): pass
   elif  k <= j : break
   else: ans += 1
 print(ans)
 ans = 0
 N,M = map(int, input().split())