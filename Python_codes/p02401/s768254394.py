while(True):
    a=input().split()
    a[0]=int(a[0])
    a[2]=int(a[2])
    if(a[1]=="?"):
        break
    elif(a[1]=="+"):
        print(a[0]+a[2])
    elif(a[1]=="-"):
        print(a[0]-a[2])
    elif(a[1]=="*"):
        print(a[0]*a[2])
    elif(a[1]=="/"):
        print(a[0]//a[2])