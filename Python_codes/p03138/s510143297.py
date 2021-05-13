N, K, *A = map(int, open(0).read().split())
ls = [0]*K.bit_length()
for c in A:
  for i in range(K.bit_length()):
    if c%2==1:
      ls[i] += 1
    c >>= 1
if ls==[]:
  print(sum(A))
  import sys
  sys.exit()
ls = ls[::-1]
s = bin(K)[2:]
m = (2**(len(s)-1))*(N-2*ls[0])
dp1 = [0]*(len(s))
dp2 = [0]*(len(s))
dp1[0] = m
for i in range(1,len(s)):
  c = s[i]
  if c=='1':
    m = (2**(len(s)-i-1))*(N-2*ls[i])
    dp1[i] = dp1[i-1]+m
    if N>2*ls[i]:
      dp2[i] = dp2[i-1]+m
    else:
      dp2[i] = max(dp1[i-1],dp2[i-1])
  else:
    dp1[i] = dp1[i-1]
    if N>2*ls[i]:
      m = (2**(len(s)-i-1))*(N-2*ls[i])
      dp2[i] = dp2[i-1]+m
    else:
      dp2[i] = dp2[i-1]
print(sum(A)+max(dp1[-1],dp2[-1]))