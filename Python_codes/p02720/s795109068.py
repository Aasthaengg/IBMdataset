K = int(input())

A = [0 for d in range(20)]
A[0] = 1
dit_max = 0


for ct in range(2,K+1):
  dit_now = 0
  while dit_max > dit_now and (A[dit_now] == A[dit_now+1]+1 or A[dit_now] == 9):
    dit_now += 1
  if dit_max > dit_now:
    A[dit_now] += 1
  elif dit_max == dit_now:
    if A[dit_now] == 9:
      dit_max += 1
      dit_now += 1
    A[dit_now] += 1
  for d in range(dit_now-1,-1,-1):
      A[d] = max(A[d+1] - 1,0)
  #if ct > 30:
    #print(ct, A)
      
ans = 0
for i in range(20):
  ans += A[i] * 10**i
print(ans)
