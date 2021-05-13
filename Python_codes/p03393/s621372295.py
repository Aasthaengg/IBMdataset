alpha = "abcdefghijklmnopqrstuvwxyz"

s = input()
if len(s) < 26:
  a = sorted(list(set(alpha) - set(s)))
  print(s+a[0])
  exit(0)

def a():
  A = [chr(i) for i in range(ord('a'), ord('z')+1)]
  B = {}
  for i in range(26):
    B[A[i]] = i
  C = [0]*26
  for i in range(len(s)):
    C[B[s[i]]] = 1
  for i in range(25, -1, -1):
    t = s[i]
    for j in range(B[s[i]]+1, 26):
      if C[j] == 0:
        return s[:i] + A[j]
    C[B[t]] = 0
  return -1

print(a())