N=input()
ok=True
for i,c in enumerate(N):
  if c!=N[len(N)-i-1]:
    ok=False
if ok:
  print("Yes")
else:
  print("No")