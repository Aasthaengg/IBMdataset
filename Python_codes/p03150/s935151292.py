s=input()
k="keyence"
t=""
for i in range(7):
  if k[i]!=s[i]:
    t+=k[:i]
    break
else:
  print("YES")
  exit()
print("YES" if t+s[i-7:]==k else "NO")
