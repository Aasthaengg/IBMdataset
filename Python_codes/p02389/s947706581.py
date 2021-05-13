dato=raw_input()
a=int(dato[:dato.find(' ')])
b=int(dato[dato.find(' '):])
A=str(a*b)
P=str(2*a+2*b)
print A+" "+P
