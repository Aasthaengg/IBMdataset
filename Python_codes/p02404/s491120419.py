while True:
    a,b = input().split()
    h=int(a)
    w=int(b)
    if h ==0 and w==0:
        break
    else:
        print(w*"#")
        if h>=3 and h>=3:
            for i in range(h-2):
                print(1*"#"+(w-2)*"."+1*"#")

            print(w * "#")
        elif h==2:
            print(w * "#")
        print("")