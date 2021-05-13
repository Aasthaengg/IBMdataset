A, B = map(int,input().split(" "))
if A+B>16:
    print(":(")
else:
    if A>8 or B>8:
        print(":(")
    else:
        print("Yay!")