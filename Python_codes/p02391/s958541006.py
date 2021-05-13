a=input()
b=a.split()
c=list()

for d in b:
    c.append(int(d))
    
a=c[0]
b=c[1]

if a>b:
    print("a > b")
    
elif a<b:
    print("a < b")
    
else:
    print("a == b")
    

