import re

s = input()
n = len(s)
k = int(input())
l = []
for i in range(26):
  m_list = [m.start() for m in re.finditer(chr(ord('a')+i), s)]
  #print(m_list)
  
  for start in m_list:
    c=1
    while start + c <= n and c <= 5:
      if not s[start:start+c] in l:
        l.append(s[start:start+c])
      c += 1
  if len(l) >= k:
    break
#print(l)
print(sorted(l)[k-1])
    
