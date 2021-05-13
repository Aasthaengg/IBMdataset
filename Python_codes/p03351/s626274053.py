a,b,c,d=map(int,input().split())
e=abs(a-b)
f=abs(b-c)
g=abs(a-c)
if g<=d:
    print("Yes")
elif e<=d and f<=d:
    print("Yes")
else:
    print("No")
