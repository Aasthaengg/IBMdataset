moji = str(input())
A,B,C,D = int(moji[0]),int(moji[1]),int(moji[2]),int(moji[3])

mojiretsu = str(A-B) + str(B-C) + str(C-D)
if ("00" in mojiretsu ):
    print("Yes")
else:
    print("No")