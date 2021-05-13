a=[]
for i in input():
    if i=="S":
        a+=i
    
    if a:
        if i=="T" and a[-1]=="T":
            a+=i
        if i=="T" and a[-1]=="S":
            a.pop(-1)
    elif i=="T" and len(a)==0:
        a+=i    
print(len(a))