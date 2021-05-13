S = input()

def findPos(s,char):
  l = []
  for i in range(len(s)):
    if s[i] == char:
      l.append(i)
  return l

A_pos = findPos(S,"A")
Z_pos = findPos(S,"Z")
print(max(Z_pos)-min(A_pos)+1)