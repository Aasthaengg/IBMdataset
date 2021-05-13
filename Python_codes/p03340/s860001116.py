N = int(input())
As = list(map(int, input().split()))
def xor(L):
  r = L[0]
  for i in range(1, len(L)):
    r ^= L[i]
  return r
re = 0
r = 0
s = 0
x = 0
for l in range(0, N):
  #s += As[l]
  #x ^= As[l]
  while r < N:
    #print(l, r, s, x)
    if s+As[r] == x^As[r]:
      s += As[r]
      x ^= As[r]
    #if sum(As[l:r+1]) == xor(As[l:r+1]):
      r += 1
    else:
      break
  s -= As[l]
  x ^= As[l]
  #print(l, r)
  re += r-l
print(re)
