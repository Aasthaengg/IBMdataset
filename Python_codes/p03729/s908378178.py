a = input().split()

ok = True
for i in range(1,len(a)):
  if a[i-1][-1]==a[i][0]:
    continue
  else:
    ok = False
print("YES" if ok else "NO")