import math
N = int(input())

def yakusu(A):
  arr = []
  limit = int(math.sqrt(A))
  for i in range(2,limit+1):
    if A % i == 0:
      arr.append(i)
      if i != A // i:
        arr.append(A//i)
  arr.append(A)
  arr.sort()
  return(arr)

yakusu_N = yakusu(N)
yakusu_N1 = yakusu(N-1)


      
def ope(a,N):
  while True:
    if N % a == 0:
      N = N / a
      if N == 1:
        return 1
        break
    else:
      N = N % a
      if N != 1:
        return 0
        break
      else :
        return 1
        break



count = 0 
for i in yakusu_N:  
  if ope(i,N) == 1:
    count += 1
if N != 2:
  print(count + len(yakusu_N1))
else:
  print(1)