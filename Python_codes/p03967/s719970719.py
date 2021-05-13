s=input()
n=len(s)

c=0
for i in range(n):
  if s[i]=="g":
    c+=1
  else:
    c-=1

c+=n%1

print(c//2)