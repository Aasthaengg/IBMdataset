x=int(input())

if x<=6:
    print("1")
    exit()
elif x<=11:
    print("2")
    exit()
else:
    ans=((x//11)*2)
    if x%11==0:
        print(ans)  
    elif x%11<=6:
        print(ans+1)
    else:
        print(ans+2)