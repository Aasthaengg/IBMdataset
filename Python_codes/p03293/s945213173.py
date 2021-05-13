s=input()
t=input()
flag=False
for i in range(len(s)):
  if s==t:
    print("Yes")
    flag=True
    break
  s=s[-1]+s[:-1]
if not flag:
  print("No")