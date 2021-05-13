while(True):
    a=list(map(int,input().split()))
    if(a[0]==0 and a[1]==0):
        break
    for x in range(a[0]):
        print("#"*a[1])
    print()