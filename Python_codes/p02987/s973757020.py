a1=input()
a2=list(a1)
b=[ord(x) for x in a2]
b.sort()
if len(a2)==4 and b[0]==b[1] and b[2]==b[3] and b[1]!=b[2]:
    print("Yes")
else:
    print("No")