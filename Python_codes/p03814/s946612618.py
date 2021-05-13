s=list(input())
a=0
z=0

for i in range(len(s)):
  if s[i]=="A":
      a=i
      break

S=list(reversed(s))
for j in range(len(S)):
    if S[j]=="Z":
        z=j
        break

print(len(s)-a-z)