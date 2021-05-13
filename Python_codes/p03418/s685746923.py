N, K = map(int, input().split())
if K == 0:
  r = N*N
  print(r)
  exit()
r = 0
for b in range(K+1, N+1):
  r0 = r
  r += (N//b)*(b-K)
  r1 = r
  r += max(0, N+1-(N//b*b+K))
  #for a in range(N//b*b+K, N+1):
    #if a%b >= K:
  #  r += 1
  #print(b, r-r0, r1-r0, r-r1)
print(r)
