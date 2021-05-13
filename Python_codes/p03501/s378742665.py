import re
 
a = input()
 
a = re.split(" ",a)
 
b = int(a[0])*int(a[1])
c = int(a[2])
 
if(b < c):
    print(b)
else:
    print(c)