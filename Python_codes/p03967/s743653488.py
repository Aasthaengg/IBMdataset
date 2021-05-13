import math
s = input()
li = list(s)
a = li.count('p')
b = li.count('g')
#print(a,b)
#1 2
risou = math.ceil((a+b)/2)
#print(risou) 2
print(((a+b)-risou)-a)