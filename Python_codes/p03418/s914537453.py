N, K = map(int, input().split())

ans = 0
for r in range(K+1,N+1):
  if K>0:
    ans += N-(N//r*K+min(N%r+1,K)-1)
  else:
    ans += N
print(ans)

#print(*ans, sep='\n')
