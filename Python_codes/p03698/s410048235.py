import sys
s=input()
t=set()
for i in range(len(s)):
  if s[i] in t:
    print('no')
    sys.exit()
  t.add(s[i])
print('yes')