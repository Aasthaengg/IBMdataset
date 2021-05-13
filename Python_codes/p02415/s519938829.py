t=list(str(raw_input()))
o=""
for i in range(len(t)):
        if t[i].isupper():
                t[i]=t[i].lower()
        elif t[i].islower():
                t[i]=t[i].upper()
for i in range(len(t)):
        o+=t[i]
print o