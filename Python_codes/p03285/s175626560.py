n=int(input())
ok=False
if n%4==0:
    print("Yes")
else:
    while n>0:
        if n%7==0:
            ok=True
            break
        n-=4
    if ok:
        print("Yes")
    else:
        print("No")