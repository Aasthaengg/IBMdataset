s=input()
z=753
for i in range(len(s)-2):
  x=int(s[i:i+3])
  y=abs(753-x)
  z=min(z,y)
print(z)

