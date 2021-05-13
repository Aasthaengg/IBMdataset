S=input()
T=input()

ok=True
a,b={},{}
for i in range(len(S)):
  s=S[i]
  t=T[i]
  if s in a:
    if a[s]!=t:
      ok=False
  if t in b:
    if b[t]!=s:
      ok=False
  a[s]=t
  b[t]=s

print("Yes" if ok else "No")
