s=input()
s=s.replace("BC","Z")
#print(s)

a=0
b=0
for i in s:
    if i=="A":a+=1
    elif i=="Z":b+=a
    else:a=0
print(b)