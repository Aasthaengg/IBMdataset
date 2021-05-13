h,w=map(int,input().split())
a=[0]*h
book={}
for _ in range(h):
    a=input()
    for i in a:
        if i in book:
            book[i]+=1
        else:
            book[i]=1


if h%2==0 and w%2==0:
    for i in book:
        if book[i]%4!=0:
            print("No")
            exit()
    print("Yes")

elif h%2==1 and w%2==1:
    cnt=0
    odd=0
    for i in book:
        if book[i]%2==1:
            odd+=1
            if odd==2:
                print("No")
                exit()
        cnt+=book[i]//4
    if odd==0:
        print("No")
    else:
        if cnt>=(h-1)*(w-1)//4:
            print("Yes")
        else:
            print("No")
else:
    cnt=0
    for i in book:
        if book[i]%2==1:
            print("No")
            exit()
        cnt+=book[i]//4
    if h%2==1:
        if cnt>=(h-1)*w//4:
            print("Yes")
        else:
            print("No")
    else:
        if cnt>=(w-1)*h//4:
            print("Yes")
        else:
            print("No")