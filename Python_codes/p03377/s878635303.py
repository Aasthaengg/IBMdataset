A,B,X = map(int,input().split())
if A>X:
    print("NO")
if A<=X:
    if (A +B)<X:
        print("NO")
    else:
        print("YES")
