x,y = map(int, input().split())
a = [4,6,9,11]
if (x==2 or y==2):
    print("No")
    exit()
elif (x in a):
    if (y in a):
        print("Yes")
    else:
        print("No")
else:
    if (y in a):
        print("No")
    else:
        print("Yes")