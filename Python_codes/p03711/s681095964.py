a,b=input().split()
list1={"1":1,"2":3,"3":1,"4":0,"5":1,"6":0,"7":1,"8":1,"9":0,"10":1,"11":0,"12":1}
c=list1[a]
d=list1[b]
if str(c)==str(d):
  print("Yes")
else:
  print("No")