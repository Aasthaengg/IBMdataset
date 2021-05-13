A,B,X = map(int,input().split(" "))
if A+B<X:
    print("NO")
else:
    if A>X:
        print("NO")
    else:
        if (X-A)>B:
            print("NO")
        else:
            print("YES")