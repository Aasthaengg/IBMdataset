N = int(input())
A = list(map(int, input().split()))
res = 0
n = 0
quot = (10 ** 9) + 7
while 1:
  p = 0
  q = 0
  temp = 0
  for i, var in enumerate(A):
    if var % 2 == 1:
      p += 1
    else:
      q += 1
    A[i] = A[i] >> 1
    temp += var
  
  if temp == 0:
    break
  res += p*q*(2**n)
  res %= quot
  n += 1
print(res)  
