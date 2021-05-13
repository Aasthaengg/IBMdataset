a="abcdefghijklmnopqrstuvwxyz"
s=input()
t=input()
ds={}
dt={}
for i in a:ds[i]=dt[i]=""
for i in range(len(s)):
  if ds[s[i]]=="":ds[s[i]]=t[i]
  elif ds[s[i]]!=t[i]:exit(print("No"))
  if dt[t[i]]=="":dt[t[i]]=s[i]
  elif dt[t[i]]!=s[i]:exit(print("No"))
print("Yes")