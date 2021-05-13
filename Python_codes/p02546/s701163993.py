a=input()
if(a[-1]=="s"):
    a.rstrip("s")
    print(a,"es",sep="")
else:
    print(a,"s",sep="")
