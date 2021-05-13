t=input()

new=""
for i in range(len(t)):
    if t[i] != "?":
        new+=t[i]
    else:
        if new=="":
            new+=t[i]
        elif new[-1]=="P":
            new+="D"
        else:
            new+=t[i]

t=new
new=""

for i in reversed(range(len(t))):
    if t[i] != "?":
        new=t[i]+new
    else:
        if new=="":
            new=t[i]+new
        elif new[0]=="D":
            new="P"+new
        else:
            new=t[i]+new

t=new
new=""

for i in range(len(t)):
    if t[i] != "?":
        new+=t[i]
    else:
        new+="D"


print(new)