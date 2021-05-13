import math
N_MAX = 1 ** 15
letters=list("abcdefghijklmnopqrstuvwxyz")
A_TO_Z = len(letters)
N = int(input())

temp = N
cnt = 1
while temp - A_TO_Z ** cnt > 0:
  temp -= A_TO_Z ** cnt
  cnt += 1
r = [0] * cnt
  
q = temp - 1
while q > 0:
  r[cnt-1] = q % A_TO_Z
  cnt -= 1
  q = q // A_TO_Z
for i in r:
  print(letters[i],end="")
