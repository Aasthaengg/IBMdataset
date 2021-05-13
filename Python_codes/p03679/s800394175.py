X,A,B = [int(i) for i in input().split()]
if B <= A:
    print("delicious")
    exit()
else:
    if B - A <=X:
        print("safe")
        exit()
    else:
        print("dangerous")
        exit()