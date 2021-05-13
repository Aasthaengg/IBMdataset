S=input()
if S=="keyence":
  print("YES")
  exit()
for i in range(7):
  T=S[:i]+S[len(S)-7+i:]
  if T=="keyence":
    print("YES")
    exit()
print("NO")