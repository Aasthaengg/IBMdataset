list=["A","B","C","D","E","F"]
a,b=[str(i) for i in input().split()]
if list.index(a)==list.index(b):
  print("=")
elif list.index(a)>list.index(b):
  print(">")
else:
  print('<')