while (True):
    a=list(map(int,input().split()))
    if (a[0]==0 and a[1]==0):
        break
    if(a[0]<a[1]):
        print(str(a[0])+" "+str(a[1]))
    else:
        print(str(a[1])+" "+str(a[0]))