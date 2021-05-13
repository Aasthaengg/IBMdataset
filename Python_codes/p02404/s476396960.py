HW = input().split()
H = int(HW[0])
W = int(HW[1])

while H != 0 or W != 0:
    for j in range(W):
        print("#", end = "")
    print("")
    if W>1:
        if H>1:
            for i in range(H-2):
                print("#", end = "")
                for j in range(W-2):
                    print(".", end = "")
                print("#", end = "")
                print("")
            for j in range(W):
                print("#", end = "")
            print("")  
    HW = input().split()
    H = int(HW[0])
    W = int(HW[1])
    print("")