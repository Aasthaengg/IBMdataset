# coding: utf-8
a=input()
b=list(a)
x=700
lis={"o":1,"x":0}
for i in b:
  y=lis[i]
  if y==1:
      x=x+100
print(x)