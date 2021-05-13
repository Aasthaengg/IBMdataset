s = input()
l = s.split()
 
 
count = 6
 
if l[0] == l[1]:
  count -= 1
if l[1] == l[2]:
  count -= 1
if l[2] == l[0]:
  count -= 1
  
print(int(count/2))
