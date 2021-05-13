s=input()
ans=False
for i,v in enumerate(s):
    if ans==False:
        if v=="A":
            a=i
            ans=True
    else:
        if v=="Z":
            z=i
print(z-a+1)