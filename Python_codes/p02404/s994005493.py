while True:
    a,b=map(int, input().split())
    if a == 0 and b == 0:
        break
    if a == 1:
        print("#" * b + "\n")
    elif a == 2:
        print(("#" * b + "\n") * a)
    else:
        print("#" * b)
        print((("#" + "." * (b-2) + "#\n") * (a-2))[0:-1])
        print("#" * b + "\n")