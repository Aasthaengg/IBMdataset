x=input()
y=x.split(" ")
a=int(y[0])
b=int(y[1])
c=int(y[2])
if(a<b and b<c):
    str="Yes"
else:
    str="No"
print(str)