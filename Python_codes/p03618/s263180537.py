A = input()

Alphabet = list("abcdefghijklmnopqrstuvwxyz")

N = len(A)
ans = N*(N-1)/2 + 1

for i in Alphabet:
  z = 0
  for j in range(len(A)):
    if i == A[j]:
      z+=1
  if z>1:
    ans -= z*(z-1)/2
    
print(int(ans))