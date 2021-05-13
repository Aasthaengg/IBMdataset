s = list(input())
l = len(s)
a=0
m=0
for i in range(l):
  if s[i]=='A' or s[i]=='C' or s[i]=='G' or s[i]=='T':
    a+=1
  else:
    a=0
  m = max(m, a)

print(m)