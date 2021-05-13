s=list(input())
n=len(s)
if n==1:
    print("YES")
    exit()
if len(set(s))==2 and n==2:
    print("YES")
    exit()
if len(set(s))<3:
    print("NO")
    exit()
    
x,y,z=s.count("a"),s.count("b"),s.count('c')
if abs(x-y)>1 or abs(y-z)>1 or abs(z-x)>1:
    print("NO")
else:
    print("YES")
