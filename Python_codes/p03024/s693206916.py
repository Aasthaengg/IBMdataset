s=str(input())
s=list(s)
t=0
for i in range(len(s)):
  if s[i]=="x":
    t=t+1
if t>=8:
  print("NO")
else:
  print("YES")