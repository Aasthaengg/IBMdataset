s = str(input())
o1 = s[::2].count('1')
e1 = s[1::2].count('0')
x = len(s)-(o1+e1) 
o2 = s[::2].count('0')
e2 = s[1::2].count('1')
y = len(s)-(o2+e2)
print(min(x,y))