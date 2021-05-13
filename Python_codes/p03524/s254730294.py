s=input()
n=len(s)
a=s.count("a")
b=s.count("b")
c=n-a-b
k=max(a,b,c)
if k<=(n+2)//3:
    print("YES")
else:
    print("NO")