s=input()
c=0
for i in s:
  if i=="p":
    c-=1
c+=len(s)//2
print(c)