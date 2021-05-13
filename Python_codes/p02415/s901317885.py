a=input()
o=''
for i in range(len(a)):
    b=str(a[i])
    if (a[i].islower()):
        b=a[i].upper()
    elif (a[i].isupper()):
        b=a[i].lower()
    o+=b
print(o)
