n = input()

s = list(n)

for i in range(len(s)):
  if(s[i] == "9"):
    s[i] = "1"
  else:
    s[i] = "9"

print(''.join(s))