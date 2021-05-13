N = int(input())
A = list(map(int, input().split()))
cumsum = [0]
cumsumx = [0]
for i in range(N):
  cumsum.append(cumsum[i] + A[i])
  cumsumx.append(cumsumx[i] ^ A[i])
res = 0
"""
for i in range(1, N + 1):
  for j in range(i, N + 1):
    #print(i, j, cumsum[j - 1] - cumsum[i], cumsumx[j] ^ cumsumx[i - 1])
    if cumsum[j] - cumsum[i - 1] == cumsumx[j] ^ cumsumx[i - 1]:
      res += 1
"""   
for i in range(1, N + 1):
  l = i
  r = N
  j = (l + r) / 2

  while True:
    j = (l + r) // 2
    if r - l < 2:
      #print(i, j, l, r)
      break
    if cumsum[j] - cumsum[i - 1] == cumsumx[j] ^ cumsumx[i - 1]:
      l = j
    else:
      r = j
  #print(i, j)
  if j < N:
    if cumsum[j + 1] - cumsum[i - 1] == cumsumx[j + 1] ^ cumsumx[i - 1]:
        j += 1
  res += j - i + 1
    
print(res)
#print(cumsum)
#print(cumsumx)
