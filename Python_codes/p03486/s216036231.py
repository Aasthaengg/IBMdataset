s=list(input())
t=list(input())
s.sort()
t.sort(reverse=True)
s="".join(s)
t="".join(t)
for i in range(min(len(s),len(t))):
  if ord(s[i])==ord(t[i]):
    continue
  elif ord(s[i])<ord(t[i]):
    print("Yes")
    break
  else:
    print("No")
    break
else:
  if len(s)<len(t):
    print("Yes")
  else:
    print("No")