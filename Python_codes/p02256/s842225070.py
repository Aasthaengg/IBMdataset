list=[int(i) for i in input().split()]



if list[0]>list[1]:
    a=list[0]
    b=list[1]
else:
    b=list[0]
    a=list[1]    


if a%b==0:
    print(b)
else:
    while b>0:
        c=a%b
        a=b
        b=c
    print(a)
