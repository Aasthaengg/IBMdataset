N = int(input())

S = input()
s = list(S)
l = len(s)



B = []

for i in range(l):
  c = ord(s[i])
  e = c+N
  if e>ord('Z'):
    e = e - 26
  d = chr(e)
  B.append(d)
    
b = ''.join(B)

print(b)
