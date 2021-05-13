s=input()
c=0
w=["SUN","MON","TUE","WED","THU","FRI","SAT"]
for i in range(7):
  if(s==w[i]):
    break
  else:
    c+=1
    
print(7-i)