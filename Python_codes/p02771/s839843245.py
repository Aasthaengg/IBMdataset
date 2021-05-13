l=input("").split(" ")
a=int(l[0])
b=int(l[1])
c=int(l[2])
if(a==b and a==c):
    print("No")
elif((a-b)*(b-c)*(c-a)==0):
    print("Yes")
else:
    print("No")