N,*L = open(0).read().split()

ans = 0
a = 0
b = 0
c = 0
for s in L:
  for j in range(len(s)-1):
    if s[j]=='A' and s[j+1]=='B':
      ans += 1
  if s[-1]=='A' and s[0]=='B':
    c += 1
  elif s[-1]=='A':
    a += 1
  elif s[0]=='B':
    b += 1
if c!=0:
  if a+b>0:
    ans += c+min(a,b)
  else:
    ans += c-1
else:
  ans += min(a,b)
print(ans)