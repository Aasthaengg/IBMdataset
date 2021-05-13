n=int(input())
s=str(input())
s=list(s)
red=0
for i in range(n):
  if s[i]=="R":
    red=red+1
if red>n/2:
  print("Yes")
else:
  print("No")