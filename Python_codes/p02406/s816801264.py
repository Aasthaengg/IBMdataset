n = int(input())
for i in range(1,n+1):
    if i%3 == 0:
        if i == n or i == n-1 or i == n-2:
            print(" "+str(i))
        else:
            print(" "+str(i),end="")
    elif i%10 == 3:
        if i == n or i == n-1 or i == n-2:
            print(" "+str(i))
        else:
            print(" "+str(i),end="")
    elif str(i).find("3") > -1:
        if i == n or i == n-1 or i == n-2:
            print(" "+str(i))
        else:
            print(" "+str(i),end="")