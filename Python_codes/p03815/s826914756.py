x = int(input())

if x <= 6:
    print(1)
else:
    ans = (x//11)*2
    if x%11 == 0:
        print(int((x/11)*2))
    elif (x//11)*11 +6 >= x:
        print(ans+1)
    else:
        print(ans+2)