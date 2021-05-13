n=int(input())
a=sorted(list(map(int,input().split())))
b=sorted(list(set(a)))
l=len(b)
if l>=4:
    print("No")
    exit()
else:
    if l==1:
        if b[0]==0:
            print("Yes")
        else:
            print("No")
    elif l==2:
        if n%3!=0:
            print("No")
        else:
            if b[0]!=0:
                print("No")
            else:
                cnt1=a.count(b[0])
                cnt2=a.count(b[1])
                if cnt2==(n//3)*2:
                    print("Yes")
                else:
                    print("No")
    else:
        if n%3!=0:
            print("No")
        else:
            cnt1=a.count(b[0])
            cnt2=a.count(b[1])
            cnt3=a.count(b[2])
            if cnt1!=n//3 or cnt2!=n//3 or cnt3!=n//3:
                print("No")
            else:
                if b[0]^b[2]!=b[1]:
                    print("No")
                else:
                    print("Yes")
