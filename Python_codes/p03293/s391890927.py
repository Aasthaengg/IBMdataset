s=list(input())
t=list(input())
if s==t:
  print("Yes")
  exit()
l=len(s)  
a=s.copy()
for i in range(l):
  a.append(a[0])
  del a[0]
  if a==t:
    print("Yes")
    exit()
print("No")