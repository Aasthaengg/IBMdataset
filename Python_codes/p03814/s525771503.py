s = input()
a=0
b=0
for i in range(len(s)):
  if s[i]=='A':
    a = i
    break
for i in range(len(s)-1,-1,-1):
  if s[i] == 'Z':
    b = i
    break
print(b-a+1)