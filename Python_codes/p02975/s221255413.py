n=int(input())
a=list(map(int,input().split()))

if 1:
    tmp=0
    for item in a:
        tmp=tmp^item
    if tmp==0:
        print("Yes")
    else:
        print("No")
else:
    tmp=0
    for item in a:
        tmp=tmp^item
    if tmp==2**len(str(bin(max(a))[2:]))-1:
        print(tmp)
        print("Yes")
    else:
        print("No")



#001 (1)
#010 (2)
#011 (3)
#001 (1)
#010 (2)
#011 (3)

#010 (2)
#011 (3)
#001 (1)

#011 (3)
#001 (1)
#010 (2)
