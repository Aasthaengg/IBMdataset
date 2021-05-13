s=str(input())
t=str(input())
temp=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
s=list(s)
t=list(t)
temps=[0]*len(temp)
tempt=[0]*len(temp)
for i in range(0,len(temp)):
  temps[i]=s.count(temp[i])
  tempt[i]=t.count(temp[i])
temps.sort()
tempt.sort()
if temps==tempt:
  print("Yes")
else:
  print("No")