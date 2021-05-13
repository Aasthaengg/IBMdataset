seq=input()

s=0
t=0
c=0

for si in seq:
    if si=="S":
        s+=1
    else:
        if s==0:
            c+=1
        else:
            s-=1
c+=s

print(c)