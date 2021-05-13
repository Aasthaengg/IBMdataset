s=input()
frag="yes"
for i in range(len(s)):
  n=s.count(s[i])
  if n >1:
    frag="no"
    break
    
print(frag)