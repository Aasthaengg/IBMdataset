s=list(input())
cflag=0
fflag=0

for i in range(len(s)):
    if (cflag==0)and(s[i]=="C"):
        cflag=1
    if (cflag==1)and(s[i]=="F"):
        fflag=1
if (cflag+fflag)==2:
    print("Yes")
else:
    print ("No")
