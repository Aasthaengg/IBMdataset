s=list(input())
swi=1
if s[0]=="A":
    if "C" in s[2:-1]:
        s=s[1:]
        s.remove("C")
        swi=0
        for i in range(len(s)):
            if not s[i].islower():
                swi=1
print("AC" if swi==0 else "WA")