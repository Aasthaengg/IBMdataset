a,b,c = map(int, input().split())
d,e,f = map(int, input().split())
g,h,i = map(int, input().split())

if a-b == d-e:
    if d-e == g-h:
        if b-c == e-f:
            if e-f == h-i:
                if a-d == b-e:
                    if b-e ==c-f:
                        if d-g == e-h:
                            if e-h ==f-i:
                                print("Yes")
                                exit()

print("No")