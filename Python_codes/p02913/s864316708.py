def z_algorithm(s):
  n = len(s)
  z = [None] * n
  z[0] = n
  
  i = 1
  j = 0
  while i < n:
    while i + j < n and s[j] == s[i + j]:
      j += 1
    z[i] = j
    if j == 0:
      i += 1
      continue
    k = 1
    while i + k < n and z[k] + k < j:
      z[i + k] = z[k]
      k += 1
    i += k
    j -= k
  return z

N = int(input())
S = input()

answer = 0
for j in range(N):
  T = S[j:]
  Z = z_algorithm(T + "$" + S)
  lenT = len(T)
  lenZ = len(Z)
  for i in range(lenT, lenZ - lenT):
    if i + Z[i] < lenZ - lenT + 1:
      answer = max(answer, Z[i])

print(answer)