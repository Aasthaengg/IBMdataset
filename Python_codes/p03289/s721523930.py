s=input()
t=0
if s[0]=="A":
    if(s[2:-1].count("C")==1):
        for i in s:
            if i!="A" and i!="C":
                if i.isupper():
                    t=0
                    break
                else:
                    t=1
if t==0:
    print("WA")
else:
    print("AC")
