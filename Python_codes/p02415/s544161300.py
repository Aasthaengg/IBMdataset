import sys

s = sys.stdin.readline().rstrip('\r\n')
ss = ''

for ii in range(len(s)):
  if 'a' <= s[ii] <= 'z':
    ss += s[ii].upper()
  elif 'A' <= s[ii] <= 'Z':
    ss += s[ii].lower()
  else:
    ss += s[ii]

print(ss)

