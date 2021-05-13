inp = input()
inp = int(inp)
a = inp//3600
b= (inp-a*3600)//60
c = inp-a*3600-b*60
a = str(a)
b = str(b)
c = str(c)
print(a+":"+b+":"+c)
