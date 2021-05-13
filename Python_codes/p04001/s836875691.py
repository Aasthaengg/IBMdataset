import sys
S = list(input())
T = [int(a) for a in S]
N = len(T)

if N == 1:
  print(T[0])
  sys.exit()
  
ans = 0
for i in range(2 ** (N-1)):
  i_ = i
  j = 1
  tmp = T[0]
  while j < N:
    #print(i,i_,j,N)
    if i_ % 2 == 0:
      tmp *= 10
      tmp += T[j]
    if i_ % 2 == 1:
      ans += tmp
      tmp = T[j]
    i_ = i_ >> 1
    j += 1
  ans += tmp
  #print(ans,i)
    
print(ans)  