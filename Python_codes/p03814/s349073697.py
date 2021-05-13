s = list(input())
for a in range(len(s)):
  if s[a] == 'A':
    break
for z in range(len(s)-1,-1,-1):
  if s[z] == 'Z':
    break
print(z-a+1)
