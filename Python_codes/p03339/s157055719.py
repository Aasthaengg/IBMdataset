n=int(input())
s=input()
a=[0]*n
a[0]=s[1:].count("E")

for i in range(1,n):
  if s[i-1]=="E" and s[i]=="E":
    a[i]=a[i-1]-1
  if s[i-1]=="W" and s[i]=="E":
    a[i]=a[i-1]
  if s[i-1]=="E" and s[i]=="W":
    a[i]=a[i-1]
  if s[i-1]=="W" and s[i]=="W":
    a[i]=a[i-1]+1
print(min(a))