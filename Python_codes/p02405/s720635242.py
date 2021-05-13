HW = input().split()
H = int(HW[0])
W = int(HW[1])

while H != 0 or W != 0:
    str1 = ["."]
    str2 = ["#"]
    for j in range(W):
        if j%2 == 0:
            str1.append("#")
            str2.append(".")
        else:
            str1.append(".")
            str2.append("#")
    for i in range(H):
        if i%2 == 0:
            for k in range(W):
                print(str2[k], end = "")
        else:
            for k in range(W):
                print(str1[k], end = "")
        print("")  
    HW = input().split()
    H = int(HW[0])
    W = int(HW[1])
    print("")