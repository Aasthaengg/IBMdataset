n=int(input())
a=input()
b=input()
c=input()
d=0
for i in range(n):
  if a[i]==b[i]==c[i]:
    continue
  elif a[i]==b[i] or b[i]==c[i] or a[i]==c[i]:
    d+=1
  else:
    d+=2
print(d)
