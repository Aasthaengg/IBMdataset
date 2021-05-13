s=input()
a,b,c=s.count("a"),s.count("b"),s.count("c")
print("NO"if abs(a-b)>1 or abs(a-c)>1 or abs(b-c)>1else"YES")