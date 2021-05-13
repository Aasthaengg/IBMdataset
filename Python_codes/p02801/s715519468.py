import string
l=string.ascii_lowercase
c=input()
for i in range(len(l)):
  if l[i]==c:
    print(l[i+1])
