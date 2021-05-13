s = input()
a = [0]*3
for i in s:
  if i=="a":
    a[0] += 1
  elif i == "b":
    a[1] += 1
  elif i =="c":
    a[2] +=1
 
if a[0]==a[1]==a[2] ==1:
  print("Yes")
else:
  print("No")