from collections import deque
alphabet = "abcdefghijklmnopqrstuvwxyz"
A = input()
d = {a:deque() for a in "abcdefghijklmnopqrstuvwxyz"}
i = 0
while i < len(A):
  d[A[i]].append(i)
  i += 1
ans = 1+len(A)*(len(A)-1)//2
i = 0
while i < 26:
  a = alphabet[i]
  ans -= len(d[a])*(len(d[a])-1)//2
  i += 1
print(ans)