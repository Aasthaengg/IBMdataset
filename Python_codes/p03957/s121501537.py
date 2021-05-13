s=input()
n=len(s)
t = 1000
u = 1000
for i in range(n):
  if s[i] == "C":
    t = i
    break
for i in range(n-1,-1,-1):
  if s[i] == "F":
    u = i
    break
if max(t,u) != 1000 and t<u:
  print("Yes")
else:
  print("No")