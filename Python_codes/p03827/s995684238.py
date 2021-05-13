d={"I":+1,"D":-1}
input()
s=input()
maxx=0
x=0
for c in s:
  x+=d[c]
  maxx=max(x,maxx)
print(maxx)