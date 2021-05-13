N = int(input())
s = input()
t = input()
kaburi = 0
if s == t:
  print(N)
else:
  for i in range(N):
    if s[-(i+1):] == t[0:i+1]:
      kaburi = len(s[-(i+1):])
  print(2*N-kaburi)
