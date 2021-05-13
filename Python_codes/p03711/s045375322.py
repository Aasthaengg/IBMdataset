x,y=map(int,input().split())
if x==y==2:
    print("Yes")
elif x==4:
    if y==6 or y==9 or y==11:
        print("Yes")
    else:
        print("No")
elif x==6:
    if y==4 or y==9 or y==11:
        print("Yes")
    else:
        print("No")
elif x==9:
    if y==6 or y==4 or y==11:
        print("Yes")
    else:
        print("No")
elif x==11:
    if y==6 or y==9 or y==4:
        print("Yes")
    else:
        print("No")


else:
    if y!=2 and y!=4 and y!=6 and y!=9 and y!=11:
        print("Yes")
    else:
        print("No")
