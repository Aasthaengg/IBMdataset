l=list(map(int,input().split()))

if(l[0]==l[1]+l[2]):
    print("Yes")
elif(l[1]==l[0]+l[2]):
    print("Yes")
elif(l[2]==l[0]+l[1]):
    print("Yes")
else:
    print("No")