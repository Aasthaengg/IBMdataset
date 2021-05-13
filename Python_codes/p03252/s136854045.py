s=input()
t=input()
d=dict()
flag=True
ds=set()
for i in range(len(s)):

  if not(t[i] in d):
    if s[i] in ds:
      flag=False
      break
    d[t[i]]=s[i]
    ds.add(s[i])
  else:
    if d[t[i]]!=s[i]:
      flag=False
      break
if flag:
  print("Yes")
else:
  print("No")