s=input()
c=0
re=s[0]
n=len(s)
for i in range(1,n):
  if s[i]!=re:
    c+=1
  re=s[i]
print(c)  