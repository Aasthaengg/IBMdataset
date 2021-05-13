from collections import Counter
s = sorted(list(Counter(list(input())).values()))[::-1]
if len(s)==1:
  if s[0]!=1:
    print("NO")
    exit()
  else:
    print("YES")
    exit()
a = s[0]
if len(s)==2:
  if s[0]==1 and s[1]==1:
    print("YES")
    exit()
  else:
    print("NO")
    exit()
for i in s:
  if a==i or a==i+1:
    continue
  else:
    print('NO')
    exit()
else:
  print("YES")
