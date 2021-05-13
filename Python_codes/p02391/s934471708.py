x=input()
y=x.split(" ")
a=int(y[0])
b=int(y[1])
if(a<b):
    str="a < b"
elif(a>b):
    str="a > b"
else:
    str="a == b"
print(str)