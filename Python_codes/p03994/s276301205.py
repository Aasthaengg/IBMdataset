s = input()
l = ''
n = int(input())
alp = [chr(ord('a')+i) for i in range(26)]
for i in range(len(s)):
  if i != len(s)-1:
    if s[i] != 'a':
      if 97+26-ord(s[i]) <= n:
        n -= (123-ord(s[i]))
        l += 'a'
      else:
        l += s[i]
    else:
      l += 'a'
  else:
    t = ord(s[i])
    if t+n <= 122:
      l += chr(t+n)
    else:
      n = n%26
      if t+n <= 122:
        l += chr(t+n)
      else:
        l += chr(t+n-26)
print(l)