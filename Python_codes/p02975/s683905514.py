n=int(input())
a=list(map(int,input().split()))
if len(set(a))>3:
    print("No")
    exit()
if a.count(0)==n:
    print("Yes")
    exit()
if n%3!=0:
    print("No")
    exit()
if len(set(a))==3:
    a.sort()
    if a.count(a[0])==n//3 and a.count(a[-1])==n//3:
        if a[0]^a[-1] in set(a):
            print("Yes")
            exit()
        else:
            print("No")
            exit()
    else:
        print("No")
        exit()
elif len(set(a))==2:
    if a.count(0)==n//3:
        print("Yes")
        exit()
    else:
        print("No")
        exit()
else:
    print("No")
    exit()