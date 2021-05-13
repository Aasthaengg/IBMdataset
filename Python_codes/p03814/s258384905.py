s=input()
a=s.index("A")
s=s[::-1]
b=s.index("Z")
b=len(s)-b-1
print(b-a+1)