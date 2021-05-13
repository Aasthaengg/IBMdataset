def resolve():
    A,V =map(int,input().split())
    B,W = map(int,input().split())
    T = int(input())
    AB =abs(A-B)
    VW = V-W

    if AB == 0 and VW ==0:
        print("YES")
        return
    elif VW <=0:
        print("NO")
        return

    if AB/VW > T:
        print("NO")
    else:
        print("YES")
resolve()