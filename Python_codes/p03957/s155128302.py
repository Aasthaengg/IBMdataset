S = input()
c =False
ok = False
for s in S:
  if s == 'C':
    c = True
  elif s == 'F' and c:
    ok = True
ans = 'Yes' if ok else 'No'
print(ans)