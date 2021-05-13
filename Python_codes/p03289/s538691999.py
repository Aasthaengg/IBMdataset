s=list(input())
if s[0]=="A" and s[2:len(s)-1].count("C")==1:
    s[0]="a"
    s[s.index("C")]="c"
    if "".join(s).islower():
        print("AC")
    else:
        print("WA")
else:
    print("WA")