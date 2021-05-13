s = int(input())
a = [0]*4
a[0] = s//1000 
s = s-a[0]*1000
a[1] = s//100
s = s-a[1]*100
a[2] = s//10
s = s-a[2]*10
a[3] = s
if(a[0]==a[1] or a[1]==a[2] or a[2]==a[3]):
  print("Bad")
else:
  print("Good")