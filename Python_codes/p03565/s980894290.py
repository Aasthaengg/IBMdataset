s=input()
t=input()

lst=[]
for i in range(len(s)-len(t)+1):
  ss=s[i:i+len(t)]
  f=True
  for a,b in zip(ss,t):
    if a!=b and a!="?":
      f=False
      break
  if f:
    st=s[:i]+t+s[i+len(t):]
    lst.append(st.replace("?","a"))
if lst==[]:
  print("UNRESTORABLE")
else:
  lst.sort()
  print(lst[0])