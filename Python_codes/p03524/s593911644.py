l=input()
a=l.count("a")
b=l.count("b")
c=l.count("c")
if all([abs(a-b)<=1,abs(a-c)<=1,abs(b-c)<=1]):
   print("YES")
else:
   print("NO")