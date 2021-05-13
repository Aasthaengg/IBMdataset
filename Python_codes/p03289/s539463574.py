strs=input()
che=True
c=True
coun=False
for i in range(0,len(strs)) :
    if(i==0):
        c=True if strs[i]=="A" else False
    else :
        if(strs[i].isupper()):
            if( (not coun) and i>=2 and i<=len(strs)-2 and strs[i]=='C'):
                coun=True
            else:
                che=False
print("AC") if che and coun and c else print("WA")

