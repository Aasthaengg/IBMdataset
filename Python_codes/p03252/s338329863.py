from collections import Counter
s=Counter(input()).most_common()
t=Counter(input()).most_common()
ans="Yes"
for i in range(min(len(s),len(t))):
  if s[i][1]!=t[i][1]:
    ans="No"
print(ans)
