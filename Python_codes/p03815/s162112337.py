n=int(input())

if n<=6:
    print(1)
elif n<=11:
    print(2)
else:
    count = (n//11)*2
    if n%11 == 0:
        print(count)
    elif n%11 <= 6:
        print(count+1)
    else:
        print(count+2)