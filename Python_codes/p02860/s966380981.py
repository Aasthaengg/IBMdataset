input()
s = input()
if len(s) % 2 !=0:
  print('No')
else:
  s1 = s[:len(s)//2]
  s2 = s[len(s)//2:]
  print("Yes" if (s1 == s2) else "No")